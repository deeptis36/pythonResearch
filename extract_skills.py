import json
import re
import sys
from collections import Counter

# Sample skills list (expandable)
SKILLS = [
    'PHP', 'AI', 'Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'Django', 'Flask', 
    'Machine Learning', 'Deep Learning', 'Data Science', 'HTML', 'CSS', 'React', 'CodeIgniter',
    'Node.js', 'SQL', 'NoSQL', 'Git', 'Laravel', 'Web Development', 'Cloud Computing'
]

def extract_skills(text):
    """Extract skills from the given text using regex matching."""
    found_skills = []
    # Normalize text to lower case for case insensitive matching
    normalized_text = text.lower()
    for skill in SKILLS:
        # Use case insensitive search with word boundaries
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', normalized_text):
            found_skills.append(skill)
    return found_skills

def clean_text(text):
    """Remove non-alphanumeric characters from the given text."""
    return re.sub(r'[^a-zA-Z0-9 #]', ' ', text)  # Change to space instead of removing

def main(args):
    # Load JSON input from command line argument
    print(args)
  
    # Uncomment this if you're planning to use input_data from command-line args
    # input_data = json.loads(args[1])

    resume_text = "I SKILLS PHP, LARAVEL, CodeIgniter, AngularJS, Angular8-17 framework, MySQL, PostgreSQL PROFESSIONAL EXPERIENCE Sr. Software Engineer | FCS Software Solutions - Noida, India  05/2024 – TILL DATE*   Led a team of 6 software engineers in the design and development of innovative healthcare software solutions.   Developed robust backend systems to support healthcare facility operations and ensure seamless functionality.  Engineered front-end components using the Angular framework, optimizing UI performance for enhanced user experience. Sr. Software Engineer | Indus Net Technologies Ltd - Noida, India  06/2019 – 05/2024."
    
    # Clean text input
    job_description = "required php laravel developer"  # clean_text(input_data.get('job_description', ''))

    # Extract skills from both resume and job description
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    # Prepare the output
    output = {
        'resume_skills': {
            'matched_skills': resume_skills,
            'skill_count': len(resume_skills),
        },
        'job_skills': {
            'matched_skills': job_skills,
            'skill_count': len(job_skills),
        },
        'matched_skills': list(set(resume_skills).intersection(job_skills)),
        'matched_skill_count': len(set(resume_skills).intersection(job_skills))
    }

    # Print the output as JSON
    print(json.dumps(output))

if __name__ == "__main__":
    main(sys.argv)
