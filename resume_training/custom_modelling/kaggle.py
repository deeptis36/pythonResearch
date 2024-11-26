from pyresparser import ResumeParser
import warnings

# Ignore UserWarnings
warnings.filterwarnings("ignore", category=UserWarning)

# Parse the resume
file = "files/Resume_140624131439_.pdf"
data = ResumeParser(file).get_extracted_data()

# Print extracted data
print("Name:", data["name"])
