import pandas as pd
import matplotlib.pyplot as plt

# Load internship dataset
internships = pd.read_csv("data/internships.csv")

print("Dataset loaded successfully!")

# display dataset
print(internships)

# dataset dimensions
print("\ndataset shape:")
print(internships.shape)


# column names
print("\ncolumn names:")
print(internships.columns)

# missing values
print("\nmissing values:")
print(internships.isnull().sum())

# duplicate rows
print("\nduplicate rows:")
print(internships.duplicated().sum())

# dataset information
print("\ndataset information:")
internships.info()

# Create a copy for cleaning
cleaned_internships = internships.copy()

# Remove duplicate rows
cleaned_internships = cleaned_internships.drop_duplicates()

# Remove unnecessary spaces from text
for column in cleaned_internships.select_dtypes(include="object").columns:
    cleaned_internships[column] = cleaned_internships[column].str.strip()

# Display cleaned dataset
print("\nCleaned dataset:")
print(cleaned_internships.head())

# Save cleaned dataset
cleaned_internships.to_csv(
    "data/cleaned_internships.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")

category_count=cleaned_internships['skills'].value_counts().head(7)
category_count.plot(kind='bar')
plt.title('top internship skills ')
plt.xlabel('skills')
plt.ylabel('number of skills')
plt.show()

cleaned_internships.to_csv("data/cleaned_internships.csv",index=False)
#location
location_count = cleaned_internships["location"].value_counts()
print("internship by location")
print(location_count)

#work types
work_types=cleaned_internships["work_type"].value_counts()
print("internship by workplace")
print(work_types)

#titles
internship_titles=cleaned_internships["title"].value_counts()
print("internships by titles")
print(internship_titles)
 #skills
print(cleaned_internships["skills"])

# Task 4 - Find most common skills

all_skills = cleaned_internships["skills"].dropna()

# Split skills separated by commas
all_skills = all_skills.str.split(",").explode()

# Remove spaces
all_skills = all_skills.str.strip()

# Remove commas and other unnecessary characters
all_skills = all_skills.str.strip(",")

# Remove empty values
all_skills = all_skills[all_skills != ""]

# Count skills
skill_count = all_skills.value_counts()

print("Most common skills:")
print(skill_count.head(10))
#top 10 skills
skill_count.head(10).plot(kind="bar")
plt.title("top 10 skills")
plt.xlabel("skills")
plt.ylabel("no. of skills")
plt.show()
cleaned_internships.to_csv("data/cleaned_internships.csv", index=False)


