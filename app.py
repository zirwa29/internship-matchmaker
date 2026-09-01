from flask import Flask, render_template, request
from src.matcher import calculate_match
import pandas as pd

app = Flask(__name__)

internships = pd.read_csv("data/cleaned_internships.csv")


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        skills = request.form["skills"]

        student_skills = [
            skill.strip().lower()
            for skill in skills.split(",")
        ]

        internships["match_score"] = internships["skills"].apply(
            lambda x: calculate_match(x, student_skills)
        )

        recommended_internships = internships.sort_values(
            by="match_score",
            ascending=False
        )

        recommendations = recommended_internships.head(5).to_dict("records")

        for internship in recommendations:

            score = internship["match_score"]

            if score >= 3:
                internship["match_level"] = "Excellent Match"
            elif score == 2:
                internship["match_level"] = "Good Match"
            elif score == 1:
                internship["match_level"] = "Average Match"
            else:
                internship["match_level"] = "Poor Match"

    return render_template(
        "index.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)