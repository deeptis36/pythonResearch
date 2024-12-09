# data.py
import spacy
import re
skill_array = [
   "testng",
    # Programming Languages
    "Java", "JavaScript", "TypeScript", "Python", "PHP", "Ruby", "C#", "C", "C++", "Swift", "Kotlin", "Go", "Rust", "R", "Scala",
    "Perl", "MATLAB", "Dart", "Shell Scripting", "VB.NET", "Groovy", "Haskell", "Lua", "Fortran", "COBOL",

    # Web Development
    "HTML", "HTML5", "CSS", "CSS3", "Bootstrap", "Tailwind CSS", "Sass", "LESS", "jQuery", "AJAX", "JSON", "XML",
    "XHTML", "ASP.NET", "ASP.NET Core", "ASP.NET MVC", "ASP.NET WebForms",

    # Frontend Frameworks
    "React", "Angular", "Vue.js", "Svelte", "Ember.js", "Backbone.js", "Preact", "LitElement",

    # Backend Frameworks
    "Spring Boot", "Django", "Flask", "Laravel", "CodeIgniter", "Symfony", "Ruby on Rails", "Express.js", "Next.js",
    "NestJS", "ASP.NET Core", "Gin (Go)", "FastAPI",

    # Databases
    "MySQL", "PostgreSQL", "SQLite", "MongoDB", "Cassandra", "Redis", "Elasticsearch", "Oracle", "MS SQL Server",
    "MariaDB", "Firebase Realtime Database", "DynamoDB", "HBase", "Neo4j", "Snowflake", "CouchDB", "Memcached",

    # DevOps & Cloud
    "Docker", "Kubernetes", "AWS", "Azure", "Google Cloud Platform (GCP)", "Heroku", "DigitalOcean", "Terraform",
    "Ansible", "Chef", "Puppet", "Vagrant", "OpenStack", "Apache Kafka", "RabbitMQ", "Nginx", "Jenkins", "CircleCI",
    "Travis CI", "GitHub Actions", "GitLab CI/CD", "Bamboo", "Azure DevOps", "AWS Lambda", "CloudFormation",

    # Machine Learning & Data Science
    "TensorFlow", "Keras", "PyTorch", "Scikit-learn", "Pandas", "NumPy", "Matplotlib", "Seaborn", "NLTK",
    "OpenCV", "Deep Learning", "Natural Language Processing", "Data Engineering", "Big Data", "Apache Spark",
    "Hadoop", "PySpark", "XGBoost", "LightGBM", "Fast.ai", "Jupyter Notebook", "RapidMiner", "Tableau", "Power BI",

    # Testing
    "JUnit", "Selenium", "Postman", "SoapUI", "Cucumber", "TestNG", "Cypress", "Playwright", "Katalon Studio",
    "Appium", "Robot Framework", "Mocha", "Chai", "Jest", "Enzyme", "xUnit", "NUnit", "SpecFlow",

    # Tools & Platforms
    "Git", "GitHub", "GitLab", "Bitbucket", "SVN", "Maven", "Gradle", "Ant", "Visual Studio Code", "Eclipse", 
    "IntelliJ IDEA", "PyCharm", "PhpStorm", "NetBeans", "Figma", "Sketch", "Adobe XD", "Photoshop", "Illustrator",
    "PostgreSQL Studio", "SQL Server Management Studio (SSMS)", "Kibana", "Grafana",

    # Microsoft Office Suite
    "Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint", "Microsoft Outlook", "Microsoft Access",
    "Microsoft OneNote", "Microsoft Teams", "Microsoft SharePoint", "Microsoft Publisher", "Microsoft Visio",
    "Microsoft Project",

    # Security
    "OAuth", "OAuth2", "JWT", "LDAP", "SAML", "OpenID Connect", "Encryption", "Firewall", "Penetration Testing",
    "OWASP", "ZAP", "Snort", "Wireshark", "SSL/TLS",

    # Mobile App Development
    "React Native", "Flutter", "Ionic", "Xamarin", "SwiftUI", "Android SDK", "iOS SDK", "Unity", "Kotlin Multiplatform",

    # Emerging Technologies
    "Blockchain", "Ethereum", "Solidity", "Hyperledger", "IoT", "AR/VR", "Edge Computing", "Quantum Computing",

    # Agile & Project Management
    "Agile", "Scrum", "Kanban", "JIRA", "Confluence", "Asana", "Trello", "Slack", "MS Project", "Basecamp",

    # API Development & Integration
    "RESTful APIs", "GraphQL", "SOAP", "WebSockets", "gRPC", "Swagger", "Postman Collections",

    # Additional Skills
    "Microservices Architecture", "Serverless Computing", "Multithreading", "Parallel Processing", "Event-Driven Architecture",
    "Search Engine Optimization (SEO)", "Content Management Systems (CMS)", "WordPress", "Drupal", "Joomla",
    "Shopify", "Magento", "E-commerce Platforms", "SAP", "Salesforce", "CRM", "ERP",
    "Data Visualization", "Data Wrangling", "Data Mining", "ETL Processes", "Azure Data Factory",
    "Windows Communication Foundation (WCF)", "Windows Presentation Foundation (WPF)",
    "LINQ", "Entity Framework", "Hibernate", "JDBC"




    "HTML", "CSS", "JavaScript", "TypeScript", "Angular", "React", "Vue.js", "Svelte",
    "Bootstrap", "Tailwind CSS", "jQuery", "AJAX", "JSON", "XML", "PHP", "Laravel", "CodeIgniter", "Symfony",
    "Python", "Django", "Flask", "Java", "Spring", "C#", ".NET", "Ruby", "Ruby on Rails", "Node.js",
    "Go", "C", "C++", "Rust", "Kotlin", "Swift", "React Native", "Flutter", "MySQL", "PostgreSQL", "SQLite", "MongoDB",
    "Cassandra", "Redis", "Elasticsearch", "Git", "GitHub", "GitLab", "Bitbucket", "Visual Studio Code", "Sublime Text",
    "Atom", "Eclipse", "IntelliJ IDEA", "PyCharm", "PhpStorm", "NetBeans", "Jenkins", "CircleCI", "Travis CI",
    "GitHub Actions", "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Amazon Web Services", "Google Cloud Platform",
    "Heroku", "DigitalOcean", "OpenStack", "TensorFlow", "Keras", "PyTorch", "Scikit-learn", "Pandas", "NumPy",
    "Machine Learning", "Artificial Intelligence", "Natural Language Processing", "Deep Learning", "Data Science",
    "Data Engineering", "Big Data", "Hadoop", "Spark", "Tableau", "Power BI", "SQL", "NoSQL", "Firebase", "Redis",
    "Elasticsearch", "API Development", "GraphQL", "RESTful Services", "WebSockets", "OAuth", "JWT", "OAuth2", "Swagger",
    "JUnit", "Selenium", "Test Automation", "TDD", "BDD", "Agile", "Scrum", "Kanban", "JIRA", "Confluence", "Asana",
    "Trello", "Postman", "Insomnia", "SoapUI", "Wireshark", "Figma", "Sketch", "Adobe XD", "Photoshop", "Illustrator",
    "Jenkins", "CircleCI", "Travis CI", "CI/CD", "Vagrant", "Terraform", "Ansible", "Chef", "Puppet", "Linux", "Unix",
    "MacOS", "Windows", "Cloud Computing", "Microservices", "Containerization", "DevOps", "Automation", "AI/ML APIs",
    "Blockchain", "Cryptocurrency", "IoT", "Embedded Systems", "Computer Vision", "Augmented Reality", "Virtual Reality",
    "UI/UX Design", "Wireframing", "Prototyping", "Branding", "Marketing Automation", "Digital Marketing", "SEO", "SEM",
    "Social Media Marketing", "Content Strategy", "Google Analytics", "Google Ads", "Facebook Ads", "LinkedIn Ads",
    "Email Marketing", "Copywriting", "Content Management", "PR", "Event Management", "Salesforce", "SAP", "ERP Systems",
    "Business Intelligence", "Financial Modeling", "Project Management", "Product Management", "Team Leadership", 
    "Stakeholder Management", "Vendor Management", "Customer Support", "Business Analysis", "Market Research", 
    "Customer Relationship Management", "E-commerce", "Retail Management","Oracle","ASP.NET Core","Java8","XHTML",
      'ASP.NET Core 6.0/7.0/8.0',"Tier Web-based"
    'ASP.NET MVC 5.0/6.0',
    'Multithreading',"Tier Web-based"
    'Data Structures',
    'Algorithms',
    'JAVA Script',
    'Cloud',
    'Function Apps',
    'App Insights',
    'Coded UI',
    'ASP.NET Web Forms',
    'Logic Apps',
    'Streams API',
    'Generics',
    'Dozer',
    'Visual Studio',
    'Kibana',
    'Stored Procedures',
    'Web Apps',
    'CI',
    'Java Persistence API',
    'Azure Cloud',
    'Angular14',
    'XHTML',
    'Razor View Engine',
    'Entity Framework 6',
    'Rest',
    'Single Sign-on',
    'Active Directory',
    'HttpClientModule',
    'Sidhi Infotech',
    'Repeater',
    'Employee Registration',
    'Login User Controls'
    # Programming Languages
    "Java", "Angular14","ASP.NET Core 6.0/7.0/8.0"
    "JavaScript", 
    "JSP", "OAuth",
    "JSF", 
    "HTML", "Solaris"
    "CSS","Microsoft Technologies","Microsoft"
    "XML", "ASP.NET",
    "SQL", "Core Java","ASP.NET WEB API","ASP.NET MVC","ASP.NET WebForms"
    "Json", "CSS5","Entity Framework","Spring Boot","Jetty","JDBC","HTML5","Apache Kafka","Cassandra DB","'ASP.NET Core"
    "ASP.NET",
    "JavaScript",
    # Frameworks & Libraries
    "Hibernate", 
    "Restful", 
    "JQuery", 
    "Richfaces", 
    "Yahoo UI", 
    "Ajax", 
    "Spring", 
    "Node.js", 
    "React", 
    # Cloud & DevOps
    "AWS", 
    "Google Cloud", 
    "Cloud Computing", 
    "Kubernetes", 
    "Docker", 
    "CI/CD", 
    "SVN", 
    "Gitlab", 
    "Jenkins",
    "SQL Server", 
    "MySQL", 
    "Sybase", 
    "Hive", 
    "Hadoop", 
    # Tools & Platforms
    "Maven", 
    "Weblogic", 
    "Apache", 
    "Jboss", 
    "SQR", 
    # Security & Operations
    "ACL", 
    "ACLs", 
    "Zscaler", 
    # Communication & Collaboration Tools
    "TikTok", 
    "LarkBot", 
    "Bytefaas", 
    "Twitter",
    "Bytedance", 
    "SentinelOne",
    "Lark",
    # Big Data & Distributed Systems
    "Kafka BMQ", 
    "DataBus", 
    "Hive DB", 
    "Analysis Rule Engine",
    "Databus",
    "Cloud Compute Engine",
    "High Intrusive Defense System",
    "Kafka",
    "Jira",
    "certified",
    "hp certified"
]
skill_array = [skill.lower() for skill in skill_array]

month_array = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

month_array = [month.lower() for month in month_array]

roles_array = [
    "Growth and Sustainability Consultant",
    "qa lead","Test Lead","Sr Test Engineer","Software Quality Assurance Tester","Software Quality Assurance Engineer",
    "qa manager",
    "qa engineer",
    ". Net Developer",
    "Software Developer Engineer",
    "sr. business process analyst","sr. software qa","sr. quality assurance engineer",
    "php developer","sr. quality assurance",
    "senior security engineer",
    "Lead Security Engineer  Architect",
    "Lead Security Engineer & Architect","Sr. Systems Security Engineer","Information Assurance Assessor",
    "Systems Deployment Engineer", "professional", "Software Engineer", "Data Scientist", "Product Manager", 
    "UX Designer", "Java Developer","assistant project Manager", "Project Manager", "Business Analyst", "DevOps Engineer", 
    "Frontend Developer", "Backend Developer", "Full Stack Developer", "Marketing Manager", "Customer Support", 
    "HR Manager", "Sales Representative", "UI Designer", "Web Developer", "Mobile Developer", "Systems Administrator", 
    "Network Engineer", "Database Administrator", "QA Engineer", "Security Analyst", "Technical Writer", 
    "Chief Executive Officer", "Chief Operating Officer", "Chief Technology Officer", "Chief Financial Officer", 
    "Project Coordinator", "Researcher", "Consultant", "Graphic Designer", "Art Director", "Operations Manager", 
    "Content Writer", "Business Development Manager", "Account Manager", "Creative Director", "Social Media Manager", 
    "Event Planner", "Copywriter", "Data Analyst", "Product Owner", "IT Specialist", "Software Architect", "Legal Advisor", 
    "Financial Analyst", "Supply Chain Manager", "Content Strategist", "SEO Specialist", "Digital Marketing Manager", 
    "Compliance Officer", "Risk Manager", "Sales Manager", "Chief Marketing Officer", "Chief Product Officer", 
    "Operations Director", "Investment Analyst", "Cloud Engineer", "Game Developer", "Technical Support Specialist", 
    "Operations Assistant", "Legal Consultant", "Executive Assistant", "Business Intelligence Analyst", 
    "Solutions Architect", "Brand Manager", "Product Designer", "Customer Success Manager", "Business Systems Analyst", 
    "E-commerce Manager", "Healthcare Administrator", "Nurse Practitioner", "Medical Director", "Physical Therapist", 
    "Data Engineer", "Marketing Executive", "Team Lead", "Administrative Assistant", "Logistics Coordinator", 
    "Retail Manager", "Financial Planner", "Accountant", "Event Coordinator", "Digital Content Creator", 
    "Email Marketing Specialist", "Influencer Marketing Manager", "Training Manager", "Recruiter", "HR Generalist", 
    "Learning & Development Manager", "Talent Acquisition Specialist", "Organizational Development Consultant", 
    "Executive Director", "Program Manager", "Corporate Trainer", "Public Relations Specialist", "Brand Strategist", 
    "Operations Analyst", "Site Reliability Engineer", "Enterprise Architect", "Quality Assurance Analyst", 
    "Cybersecurity Specialist", "Cloud Solutions Architect", "System Analyst", "IT Project Manager", 
    "Business Operations Manager", "Client Relationship Manager", "Chief Risk Officer", "B2B Marketing Manager", 
    "Community Manager", "Sales Engineer", "Network Administrator", "Product Marketing Manager", 
    "Business Strategy Analyst", "User Interface Developer", "Database Developer", "Mobile App Developer", 
    "Cloud Solutions Engineer", "Cybersecurity Engineer", "Web Designer", "Help Desk Technician", "Operations Supervisor", 
    "Supply Chain Analyst", "Content Manager", "Marketing Director", "Retail Assistant Manager", "Financial Controller", 
    "Brand Ambassador", "E-commerce Specialist", "Legal Manager", "User Experience Researcher", "Customer Experience Specialist", 
    "Lead Generation Specialist", "Project Director", "HR Director", "Recruitment Manager", "Strategic Partnerships Manager", 
    "Digital Strategist", "Enterprise Sales Manager", "Financial Controller", "Product Development Manager", 
    "Head of Operations", "Lead Software Engineer", "Mobile UI/UX Designer", "Regional Sales Manager", "Director of Marketing", 
    "Client Success Manager", "SEO Manager", "Branding Consultant", "Content Marketing Manager", "Creative Writer", 
    "Senior Consultant", "Cultural Advisor", "Business Analyst Lead", "Corporate Communications Manager", 
    "Operations Executive", "Cloud Administrator", "Database Architect", "DevOps Specialist", "Network Architect", 
    "Sustainability Consultant", "Supply Chain Executive", "Project Specialist", "Commercial Manager", "Quality Manager", 
    "Service Delivery Manager", "Procurement Manager", "Compliance Manager", "Enterprise Sales Representative", 
    "Account Executive", "Social Media Strategist", "IT Security Consultant", "Process Improvement Specialist", 
    "R&D Manager", "Systems Analyst", "Cloud Operations Manager", "Public Relations Manager", "Healthcare Consultant", 
    "Fundraising Manager", "Accountant General", "Production Manager", "Project Officer", "Content Development Manager", 
    "Recruitment Officer", "Systems Engineer", "Financial Risk Manager", "Compliance Analyst", "Client Account Manager", 
    "Operations Consultant", "Investment Banker", "Legal Counsel", "Branding Manager", "Web Architect", 
    "Chief Data Officer", "Real Estate Manager", "Financial Controller", "Employee Relations Manager", 
    "Director of Operations", "Technology Consultant", "Supply Chain Director", "Product Marketing Director", 
    "Director of HR", "E-commerce Director", "Content Editor", "HR Business Partner", "Chief People Officer", 
    "HR Director", "Employee Experience Manager", "Sustainability Director", "Project Lead", "Organizational Development Specialist"
]

roles_array = [role.lower() for role in roles_array]


resume_classification = [
    "professional summary",
    "profile",
    "skills",
    "professional experience",
    "Personal Experience",
    "education",
    "projects",
    "certifications",
    "languages",
    "interests",
    "employment history",
    "references",
    "publications",
    "awards",
    "employment summary",
    "summary",
    "work experience",
    "work history",
    "summery",
    "about me",
    "programming languages",
    
]
resume_classification = [classification.lower() for classification in resume_classification]



company_names = [
    "Amazon",
    "Google",
    "Microsoft",
    "IBM",
    "Apple",
    "Facebook",
    "Twitter",
    "Netflix",
    "Tesla",
    "Oracle",
    "Adobe",
    "Salesforce",
    "Intel",
    "Nvidia",
    "Cisco",
    "Intel",
    "Qualcomm",
    "hp",
    "IBM",
]
company_names = [companyname.lower() for companyname in company_names]

responsibility_keywords = ["responsible", "led", "managed", "handled", "developed", "coordinated", "oversaw", "worked on", "supervised"]
responsibility_keywords = [responsibility.lower() for responsibility in responsibility_keywords]



work_keywords = [
    # Common phrases
  
    "work history",
    "professional summary",    
    "professional experience",    
    "employment history",
    "employment summary",
    "work experience",
    "work history",
    "Technical Skills",
    "QA TESTING EXPERIENCE",
    # Synonyms and variations
    "career summary",
    "career history",
    "job experience",
    "job history",
    "career overview",
    "employment overview",
    "employment details",
    "employment experience",
    "job details",

    # Variations with prefixes
    "summary of experience",
    "summary of employment",
    "experience overview",
    "experience details",
    "employment highlights",
    "career highlights",
    "job highlights",

    # Informal or less structured terms
    "previous jobs",
    "past jobs",
    "roles and responsibilities",
    "positions held",
    "job roles",
    "professional journey",
    "work record",
    "career path",
    "experience summary",

    # Abbreviated terms
    "exp",  # Short for experience
    "job exp",
    "work exp",
    "career exp",

    # Titles and categories
    "positions",
    "roles",
    "assignments",
    "occupations",
    "engagements",

    # Contextual or industry-specific terms
    "project experience",
    "field experience",
    "industry experience",
    "consulting experience",
    "freelance experience",
    "contract work",
    "internship experience",
    "training experience",

    # Other possible sections that overlap with work experience
    "related experience",
    "relevant experience",
    "key experience",
    "major achievements",
    "notable projects",
]
work_keywords = [work.lower() for work in work_keywords]




degrees = [
    # Associate Degrees
    "Associate of Arts (AA)",
    "Associate of Science (AS)",
    "Associate of Applied Science (AAS)",
    "Associate of Engineering (AE)",
    "Associate of Fine Arts (AFA)",

    # Bachelor's Degrees
    "Bachelor of Arts (BA)",
    "Bachelor of Science (BS)",
    "Bachelor of Fine Arts (BFA)",
    "Bachelor of Business Administration (BBA)",
    "Bachelor of Engineering (BE)",
    "Bachelor of Technology (BTech)",
    "Bachelor of Architecture (BArch)",
    "Bachelor of Commerce (BCom)",
    "Bachelor of Laws (LLB)",
    "Bachelor of Medicine and Bachelor of Surgery (MBBS)",
    "Bachelor of Computer Science (BCS)",
    "Bachelor of Nursing (BSN)",

    # Master's Degrees
    "Master of Arts (MA)",
    "Master of Science (MS)",
    "Master of Business Administration (MBA)",
    "Master of Engineering (MEng)",
    "Master of Technology (MTech)",
    "Master of Fine Arts (MFA)",
    "Master of Laws (LLM)",
    "Master of Public Health (MPH)",
    "Master of Social Work (MSW)",
    "Master of Computer Applications (MCA)",

    # Doctoral Degrees
    "Doctor of Philosophy (PhD)",
    "Doctor of Science (DSc)",
    "Doctor of Engineering (DEng)",
    "Doctor of Business Administration (DBA)",
    "Doctor of Medicine (MD)",

    # Professional Degrees
    "Juris Doctor (JD)",
    "Doctor of Dental Surgery (DDS)",
    "Doctor of Pharmacy (PharmD)",
    "Doctor of Veterinary Medicine (DVM)",
    "Doctor of Education (EdD)",
    "Doctor of Osteopathic Medicine (DO)",
    "Doctor of Public Health (DrPH)",
]
degrees = [degree.lower() for degree in degrees]






software_tools = [
    "salesforce",
    "google analytics",
    "google ads",
    "google sheets",
    "google forms",
    "google drive",
    "google calendar",
    "google maps",
    "google maps api",]
software_tools = [tool.lower() for tool in software_tools]




other_than_work_section = list(set(resume_classification) - set(work_keywords))

def check_line_contains_work_keywords(line):
    clean_text = re.sub(r'[^\w\s,.]', ' ', line)  # Remove special chars except commas and spaces
    word_count = wordcount_int_text(line)
    if word_count == 0:
        return False
    # if word_count > 3:
    #     return False
    
    # print(f"[LINE]- {line}")
    words = clean_text.split(",")
   
    for word in words:
        # print(f"[WORD]- {word}\n")
        if word in work_keywords:
            # print(f"[MATCH]- {word}")
            return True

    return False
def check_line_contains_other_than_work_keywords(line):
    clean_text = re.sub(r'[^\w\s,.]', ' ', line)  # Remove special chars except commas and spaces
    word_count = wordcount_int_text(line)
    if word_count == 0:
        return False
    if word_count > 3:
        return False
    

    words = clean_text.split()
    for word in words:
        if word in other_than_work_section:
            return True

    return False


def wordcount_int_text(text):
    word_count =0
    for word in text.split():
        if len(word.strip()) > 0:
            word_count += 1
    
    return word_count


def is_partial_match(line, reserved_keywords):
    """
    Check if any reserved keyword partially matches the provided line.

    Args:
        line (str): The input text to search within.
        reserved_keywords (list): A list of reserved keywords to match.

    Returns:
        bool: True if any keyword partially matches, False otherwise.
    """
    line_normalized = line.strip().lower()  # Normalize the line (trim and lowercase)
    
    for keyword in reserved_keywords:
        if keyword.lower() in line_normalized:  # Check for partial match
            return True
    
    return False  # No match found
