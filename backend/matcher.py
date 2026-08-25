import pandas as pd
internship=pd.read_csv("data/cleaned_internships.csv")
print("internship data loaded")
print(internship.head())
student_skills=["python","pandas","SQL"]
print("student skills:",student_skills) 

def calculate_match(student_skills,internship_skills):
    student_skills=[skill.strip().lower()for skill in student_skills]
    internship_skills=[skill.strip().lower()for skill in internship_skills.split(",")]
    match_internship=set(student_skills)&set(internship_skills)
    if len(internship_skills)==0:
        return 0
    match_internship=len(match_internship)/len(internship_skills)*100
    return match_internship

for index,internship in internship.iterrows():
    score=calculate_match(student_skills,internship["skills"])
    print(internship["company"]," -",internship["title"],"score","",score,"%")
