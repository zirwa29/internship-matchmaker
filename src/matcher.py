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

def get_matched_skills(internship_skills,student_skills):
    internship_skills=[skill.strip().lower()
                      for skill in internship_skills.split(",")
                       ]
    student_skills=[skill.strip().lower()
                    for skill in student_skills
                    ]
    matched_skills=set(internship_skills)&set(student_skills)
    return ", ".join(matched_skills)


def get_match_percentage(internship_skills, student_skills):

    internship_skills = [
        skill.strip().lower()
        for skill in internship_skills.split(",")
    ]

    student_skills = [
        skill.strip().lower()
        for skill in student_skills
    ]

    matched_skills = set(internship_skills) & set(student_skills)

    if len(internship_skills) == 0:
        return 0

    return round(
        (len(matched_skills) / len(internship_skills)) * 100
    )

def get_match_level(percentage):
        if percentage >= 80:
          return "Excellent"
        elif percentage >= 60:
          return "Good"
        elif percentage >= 40:
          return "Average"
        else:
          return "Poor"
 


# Calculate match score
internships["match_score"] = internships["skills"].apply(
    lambda x: calculate_match(x, student_skills)
)

# Calculate matched skills
internships["matched_skills"] = internships["skills"].apply(
    lambda x: get_matched_skills(x, student_skills)
)

# Calculate match percentage
internships["match_percentage"] = (
    internships["match_score"] /
    internships["skills"].str.split(",").str.len()
) * 100

# Round percentage
internships["match_percentage"] = internships["match_percentage"].round(1)

# Calculate match level
internships["match_level"] = internships["match_percentage"].apply(get_match_level)
                                                                   
                                                                   
                          
# Sort
internships = internships.sort_values(
    by="match_percentage",
    ascending=False
)

# Remove zero matches
recommended = internships[internships["match_score"] > 0]

# Get top 5
top_recommendations = recommended.head(5)

# Display
print("\n===== TOP INTERNSHIP RECOMMENDATIONS =====")

for index, internship in top_recommendations.iterrows():
    print("\n-----------------------------")
    print(f"Company: {internship['company']}")
    print(f"Title: {internship['title']}")
    print(f"Location: {internship['location']}")
    print(f"Match: {internship['match_percentage']}%")
    print(f"Level: {internship['match_level']}")
    print(f"Matched Skills: {internship['matched_skills']}")

# Save
recommended.to_csv(
    "data/recommended_internships.csv",
    index=False
)