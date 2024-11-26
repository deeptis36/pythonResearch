from pyresparser import ResumeParser
# Provide the path to your resume file (PDF, DOCX, etc.)
folder_path = "/home/preeti/Downloads/Resume_091023125848_/"
resume_path = folder_path + 'Resume_140624131439_.pdf'  # Change this to the actual path
data = ResumeParser(resume_path).get_extracted_data()

# Print the extracted data
print(data)