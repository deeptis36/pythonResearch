import os
import pandas as pd
import nltk
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

from pyresparser import ResumeParser

def main():
    try:
        # Parse resume PDF using pyresparser
        resume_file = os.path.join("/var/www/html/ml/app/scripts", "docs", "resume.pdf")
        resume_data = ResumeParser(resume_file).get_extracted_data()
        if resume_data is None:
            print("Error: Unable to extract data from the resume.")
            return
        print("Extracted Resume Data:")
        print(resume_data)

        # Save the parsed data into resume.txt
        resume_text_file = os.path.join("/var/www/html/ml/app/scripts", "docs", "resume.txt")
        with open(resume_text_file, "w", encoding='utf-8') as rf:
            rf.truncate()  # Clear existing content
            rf.write(str(resume_data))

        print(f"Resume data saved to {resume_text_file}")

        # Load the skills list from the CSV file
        skills_file = os.path.join("/var/www/html/ml/app/scripts", "docs", "skills.csv")
        if not os.path.exists(skills_file):
            print(f"Error: Skills file not found at {skills_file}")
            return

        skills_data = pd.read_csv(skills_file, header=None)
        skills = [skill.lower() for skill in skills_data[0].tolist()]  # Assuming skills are in the first column

        # Extract skills from the resume
        skill_list = []
        # Convert resume_data dict to string to match skills
        resume_text = ' '.join([str(value) for value in resume_data.values() if value])

        # Process the resume text using spaCy
        doc = nlp(resume_text)
        
        # Optional: Print tokens and their POS tags
        print("\nTokens and their Part-of-Speech tags:")
        for token in doc:
            print(f"{token.text}: {token.pos_}")

        for skill in skills:
            if skill in resume_text.lower():
                skill_list.append(skill)

        print("Extracted Skills from Resume:")
        print(skill_list)

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
