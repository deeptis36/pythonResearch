import PyPDF2
import re
from docx import Document

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

# Function to extract basic information
def extract_basic_info(text):
    name_pattern = r'([A-Z][a-z]+\s[A-Z][a-z]+)'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?(\(?\d{1,4}\)?[-.\s]?)?(\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4})'

    name = re.findall(name_pattern, text)
    email = re.findall(email_pattern, text)
    phone = re.findall(phone_pattern, text)

    return {
        "Name": name[0] if name else None,
        "Email": email[0] if email else None,
        "Phone": phone[0] if phone else None
    }

# Function to extract skills
def extract_skills(text, skills):
    found_skills = []
    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills


def extract_education(resume_text):
    """
    Extract education details (degree, university, and year) from a given resume text.
    """
    # Regex pattern to match education details (degree, university, year)
    education_pattern = re.compile(r'([A-Za-z0-9]+(?: [A-Za-z0-9]+)*)(?:[|,;]?\s*(.*?))?\s*(\d{4}|\w{4})')
    # education_pattern = re.compile(r'([A-Za-z]+(?: [A-Za-z]+)*)(?: \| (.*?))? (\d{4})')

    # Find all matches for education details
    education_matches = education_pattern.findall(resume_text)

    # Print each match to inspect it
    # print("Education Matches:", education_matches)

    # Extracted Education
    education = []
    for match in education_matches:
        degree, university, year = match
        # print(f"Degree: {degree}, University: {university}, Year: {year}")  # Debugging
        education.append({
            'Degree': degree.strip(),
            'University': university.strip() if university else "Not Provided",
            'Year': year
        })
    
    return education


# Main function
def parse_resume(file_path, skills_list):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        return "Unsupported file type"

    basic_info = extract_basic_info(text)
    skills = extract_skills(text, skills_list)

    return {
        "Basic Information": basic_info,
        "Skills": skills,
        "Education": extract_education(text)
    }

# Example usage
resume_path = 'resume.pdf'  # Or 'resume.docx'
skills_list = [
    'Python', 'Java', 'JavaScript', 'C++', 'C', 'C#', 'Ruby', 'PHP', 'Swift', 'Kotlin', 
    'TypeScript', 'Go', 'Rust', 'Lua', 'R', 'MATLAB', 'Dart', 'Objective-C', 'SQL', 
    'HTML', 'CSS', 'Shell scripting', 'Perl', 'Julia', 'React.js', 'Angular', 'Vue.js', 
    'jQuery', 'Svelte', 'Bootstrap', 'Tailwind CSS', 'Express.js', 'Node.js', 'ASP.NET', 
    'Laravel', 'Django', 'Flask', 'Ruby on Rails', 'Spring', 'AngularJS', 'Ember.js', 
    'Backbone.js', 'Gatsby.js', 'Android', 'iOS', 'React Native', 'Flutter', 'Xamarin', 
    'MySQL', 'PostgreSQL', 'MongoDB', 'SQLite', 'Oracle', 'Microsoft SQL Server', 'Redis', 
    'Firebase', 'Cassandra', 'DynamoDB', 'Elasticsearch', 'Amazon Web Services', 'Microsoft Azure', 
    'Google Cloud Platform', 'IBM Cloud', 'DigitalOcean', 'Heroku', 'Kubernetes', 'Docker', 
    'Terraform', 'CloudFormation', 'Git', 'GitHub', 'GitLab', 'Bitbucket', 'SVN', 'Jenkins', 
    'CircleCI', 'Travis CI', 'Docker', 'Kubernetes', 'Terraform', 'Ansible', 'Chef', 'Puppet', 
    'Vagrant', 'Selenium', 'Jest', 'Mocha', 'Jasmine', 'JUnit', 'PyTest', 'Postman', 'Cucumber', 
    'TestNG', 'Chai', 'TensorFlow', 'Keras', 'PyTorch', 'Scikit-learn', 'Pandas', 'Numpy', 
    'OpenCV', 'NLTK', 'SpaCy', 'Hugging Face', 'MATLAB', 'Apache Spark', 'R', 'XGBoost', 'Excel', 
    'Google Analytics', 'Power BI', 'Tableau', 'Matplotlib', 'Seaborn', 'Plotly', 'D3.js', 
    'Hadoop', 'Apache Spark', 'Apache Kafka', 'Apache Flink', 'Hive', 'Pig', 'Ethereum', 'Solidity', 
    'Bitcoin', 'Smart Contracts', 'Web3.js', 'Hyperledger', 'Cryptography', 'Adobe XD', 'Figma', 
    'Sketch', 'InVision', 'Photoshop', 'Illustrator', 'Balsamiq', 'Zeplin', 'Adobe After Effects', 
    'Elasticsearch', 'Kibana', 'Grafana', 'Prometheus', 'Logstash', 'Zabbix', 'Redmine', 'Jira', 
    'Confluence', 'Salesforce', 'SAP', 'ServiceNow', 'Jira', 'Confluence', 'Trello', 'Slack', 
    'Notion', 'Monday.com', 'Communication', 'Problem-solving', 'Leadership', 'Teamwork', 
    'Critical Thinking', 'Time Management', 'Negotiation', 'Collaboration', 'LaTeX', 'VBA', 
    'AutoCAD', 'Unity', 'Unreal Engine', 'SketchUp', 'Figma', 'Adobe Photoshop', 'Adobe Illustrator',
]



parsed_data = parse_resume(resume_path, skills_list)
print(parsed_data)
