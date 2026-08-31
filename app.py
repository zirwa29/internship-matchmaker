from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return "Internship Matchmaker API is running!"


@app.route("/recommendations")
def recommendations():

    skills = request.args.get("skills")

    if not skills:
        return jsonify({
            "error": "Please provide skills"
        }), 400

    student_skills = [
        skill.strip().lower()
        for skill in skills.split(",")
    ]

    internships = pd.read_csv("data/internships.csv")

    def calculate_match(internship_skills):

        internship_skills = [
            skill.strip().lower()
            for skill in internship_skills.split(",")
        ]

        matched_skills = set(student_skills) & set(internship_skills)

        return len(matched_skills)

    internships["match_score"] = internships["skills"].apply(
        calculate_match
    )

    internships = internships[internships["match_score"] > 0]

    internships = internships.sort_values(
        by="match_score",
        ascending=False
    )

    top_internships = internships.head(5)

    return jsonify(
        top_internships.to_dict(orient="records")
    )


if __name__ == "__main__":
    app.run(debug=True)