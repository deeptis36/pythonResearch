from resume_parser import resumeparse

def extract_job_role(file_path):
    # Parse resume using resumeparse
    parsed_data = resumeparse.read_file(file_path)
    
    # Extract job role (often under 'designation' or 'experience' sections)
    if 'designation' in parsed_data and parsed_data['designation']:
        job_roles = parsed_data['designation']
    elif 'experience' in parsed_data:
        job_roles = [exp['designation'] for exp in parsed_data['experience'] if 'designation' in exp]
    else:
        job_roles = []
    
    return job_roles

# Example usage
file_path = 'files/resume.pdf'
job_roles = extract_job_role(file_path)
print("Extracted Job Roles:", job_roles)




