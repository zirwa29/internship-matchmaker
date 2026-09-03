from flask import Flask, render_template, request
from src.matcher import (
    calculate_match,
    get_matched_skills,
    get_match_percentage,
    get_match_level
)
import pandas as pd

app = Flask(__name__)

internships = pd.read_csv("data/cleaned_internships.csv")


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        skills = request.form["skills"]
        location = request.form["location"]
        work_type = request.form.get("work_type", "Any")
        

        student_skills = [
            skill.strip()
            for skill in skills.split(",")
        ]

        internships["match_score"] = internships["skills"].apply(
            lambda x: calculate_match(x, student_skills)
        )

        internships["matched_skills"] = internships["skills"].apply(
            lambda x: get_matched_skills(x, student_skills)
        )

        internships["match_percentage"] = internships["skills"].apply(
            lambda x: get_match_percentage(x, student_skills)
        )

        internships["match_level"] = internships["match_percentage"].apply(
            get_match_level
        )

        filtered_internships = internships[
            internships["match_score"] > 0
        ]

        if location != "Any":
            filtered_internships = filtered_internships[
                filtered_internships["location"].str.lower() == location.lower()
            ]

        if work_type != "Any":
            filtered_internships = filtered_internships[
            filtered_internships["work_type"].str.lower() == work_type.lower()
             ]



        recommendations = filtered_internships.sort_values(
            by="match_percentage",
            ascending=False
        ).head(5)

        recommendations = recommendations.to_dict("records")

    return render_template(
        "index.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)