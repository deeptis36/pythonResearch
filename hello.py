# extract_skills.py
import spacy
import sys
import json

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

SKILL_LIST = ["Python", "Laravel", "JavaScript", "PHP", "React", "Django", "SQL", "CSS", "HTML", "Machine Learning", "AI", "NLP"]

def extract_skills(text):
    doc = nlp(text)
    extracted_skills = set()
    for token in doc:
        if token.text in SKILL_LIST:
            extracted_skills.add(token.text)
    return list(extracted_skills)

def calculate_match(resume_skills, job_skills):
    matched_skills = set(resume_skills).intersection(set(job_skills))
    match_percentage = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0
    return match_percentage, matched_skills

if __name__ == "__main__":
    input_data = json.loads(sys.argv[1])
    resume_text = input_data['resume_text']
    job_description = input_data['job_description']

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    match_percentage, matched_skills = calculate_match(resume_skills, job_skills)

    result = {
        "match_percentage": match_percentage,
        "matched_skills": list(matched_skills)
    }

    print(json.dumps(result))
