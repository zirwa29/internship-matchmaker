import pandas as pd

internships = pd.read_csv("data/cleaned_internships.csv")

print("Internship data loaded successfully!")
print(internships.head())


student_skills = [
    "Python",
    "pandas",
    "sql"
]


def calculate_match(internship_skills, student_skills):

    internship_skills = [
        skill.strip().lower()
        for skill in internship_skills.split(",")
    ]

    student_skills = [
        skill.strip().lower()
        for skill in student_skills
    ]

    matched_skills = set(internship_skills) & set(student_skills)

    return len(matched_skills)


internships["match_score"] = internships["skills"].apply(
    lambda x: calculate_match(x, student_skills)
)


internships = internships.sort_values(
    by="match_score",
    ascending=False
)


print("\nBest internship matches:")

print(
    internships[
        ["company", "title", "skills", "match_score"]
    ].head(5)
)