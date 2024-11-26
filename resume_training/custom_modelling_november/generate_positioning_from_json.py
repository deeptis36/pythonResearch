import spacy
import re
# Load the spaCy model
nlp = spacy.load('en_core_web_sm')
skill_array = [
    "HTML", "CSS", "JavaScript", "TypeScript", "Angular", "React", "Vue.js", "Svelte",
    "Bootstrap", "Tailwind CSS", "jQuery", "AJAX", "JSON", "XML", "PHP", "Laravel", "CodeIgniter", "Symfony",
    "Python", "Django", "Flask", "Java", "Spring", "Hibernate", "C#", ".NET", "Ruby", "Ruby on Rails", "Node.js",
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
    "Customer Relationship Management", "E-commerce", "Retail Management",

    # Programming Languages
    "Java", 
    "JavaScript", 
    "JSP", 
    "JSF", 
    "HTML", 
    "CSS", 
    "XML", 
    "SQL", 
    "Json", 
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
    "Jira"
]


roles_array = [
    "Software Engineer", "Data Scientist", "Product Manager", "UX Designer","Java Developer", 
    "Project Manager", "Business Analyst", "DevOps Engineer", "Frontend Developer", 
    "Backend Developer", "Full Stack Developer", "Marketing Manager", 
    "Customer Support", "HR Manager", "Sales Representative", "UI Designer", 
    "Web Developer", "Mobile Developer", "Systems Administrator", "Network Engineer",
    "Database Administrator", "QA Engineer", "Security Analyst", "Technical Writer", 
    "Chief Executive Officer", "Chief Operating Officer", "Chief Technology Officer", 
    "Chief Financial Officer", "Project Coordinator", "Researcher", "Consultant",
    "Graphic Designer", "Art Director", "Operations Manager", "Content Writer", 
    "Business Development Manager", "Account Manager", "Creative Director", 
    "Social Media Manager", "Event Planner", "Copywriter", "Data Analyst",
    "Product Owner", "IT Specialist", "Software Architect", "Legal Advisor", 
    "Financial Analyst", "Supply Chain Manager", "Content Strategist", "SEO Specialist",
    "Digital Marketing Manager", "Compliance Officer", "Risk Manager", 
    "Sales Manager", "Chief Marketing Officer", "Chief Product Officer", 
    "Operations Director", "Investment Analyst", "Cloud Engineer", "Game Developer"
]
resume_text = "Hongqian Liu\nEmail: liuhongqian@gmail.com  \t\t\tPhone: 571-296-2043\nAddress: 43450 postrail sq, Ashburn VA, 20147\t\tWork Authorization: U.S.A. Citizen\n\nExpertise Summary\nJAVA web based GUI application (Java, JSP, JSF, JavaScript, JQuery, Yahoo UI, Richfaces, Ajax, CSS, HTML,  j2ee,  Spring boot, XML, Json, SOAP web services, Hibernate, Restful microservices etc).\nPython, FaaS, Cloud, Web Services development. \nDatabase skills (Oracle, SQL Server, Hive, MySql, Sybase, Postgres 9.5 etc)\nTax and finance applications: Wash Sales; K-1 partnership; eLKE (like kind exchange), Cost Segregation application, eAdvisor (financial planning tool), CMECF/CVB case management system, Unanet financial application, Federal Home Loan Bank bond issues, Debts servicing etc\nFamiliar Programming Environments: \nOS: Windows, Unix, Linux etc\nApplication Servers: JBoss, Apache Tomcat, Websphere, Weblogic, JRun, IIS \nOther tools and languages: Maven, Ant, Jenkins, CICD, SCM, Gitlab, Github, Python, Aeolus, Hive DB, MySql, Dorado, Bytefaas, Cloud Computing Engine, JIRA, SourceSafe, SVN, CVS, Eclipse, Coldfusion, PowerBuilder, C, Perl, Agile development, Liquibase, Kubernetes etc.\n\n\nProfessional Experience\nTikTok–  Washington, DC\t\t\t  \t\t\t\t08/2022 – Current\nGlobal Security Organization - Senior Security Operation Engineer\nWorking in TikTok, my major responsibilities were developing tools and creating reports to protect user data:\nxACL LarkBot project: I developed a lark bot using Bytefaas and Python 3 to automate this process:\n\t1. Analyze users access control list (ACL) and find out inactive/expired ACLs\n\t2. Implement Lark Bot to read ACLs from Hive DB and MySQL DB. Then Lark Bot sends notice cards of expired ACLs to users\n\t3. Receive user’s responses from Lark, and save them to Lark Sheet.\n\t4. Send logs to Kafka BMQ through Databus and Topics.\n\t5. This Lark Bot can be triggered by Timer at 8AM everyday, and by command/http in Lark.\n\nThis process not only automated the current manual ACL cleanup process, reduced human effort, and sped up processing hundreds of expired ACLs every day, but also lowered the possibility of human errors during manual process. \n\nByteSiem data ingestion, security analysis and alarm rules creation:\nI imported Zimperium, Zscaler, DLP etc data sources into ByteSiem which is a centralized data storage and analysis center. My work includes:\n Created ByteFaas functions using python to read, parse, transform and extract important data \t\tfrom  AWS S3/SQS and Message Queue(BMQ), then send over processed data into ByteSiem.\n Create alarm rules using Analysis Rule Engine component in ByteSiem to analyze data stream \t\tand generate alarms based on customized data filter and configurations. Then send alarms to \t\tusers or groups by Lark message or emails.\n Migrated Splunk dashboards into ByteSiem dashboard center.\nDuring these processes, I used Python 3, Kafka BMQ, Bytefaas, TCC, Splunk, Siem and Amazon AWS S3 and SQS services,  \n\nAeolus Dashboards: I created more than 20 Aeolus dashboard reports for a variety of TikTok teams to help them better manage the risks of user data. They include but not limited:\nFuse Center Twitter dashboards. I developed Python code to call Twitter APIs to get the twitter user data mentioning TikTok and Bytedance; Created Hive table and views to store these data; Created Several Aeolus dashboard reports to analyze the usage of Tiktok tags by Twitter users.\nSentinelOne dashboard. Created Python functions in Dorado to call SentinelOne APIs to collect data; Saved data into Hive DB table and view; Migrated several SentinelOne dashboards from Splunk to Aeolus.\nHIDS dashboards: Created dashboards for High Intrusive Defense System project\nI used Python 3, Kafka BMQ, Bytefaas, Dorado, Lark APIs, Twitter APIs, Hive DB, MySql DB, Aeolus Dashboard, CICD (Gitlab code management, SCM compiling, Goofy deployment) and Cloud Compute Engine.\n\nFederal Home Loan Bank –  Reston, VA\t\t\t  \t\t02/2020 – 08/2022\nSenior Application Development Analyst\nWorking in FHLB Office of Finance, my major responsibilities are developing new functions of a varieties of financial applications:\nDebt Servicing System(DSS), which automates calculation of index rates for Bond SOFR and LIBOR etc. It also generates financial reports and exception reports , then send them to business and management teams by emails. \nOn-Network-Fedline project, which rewrites the BACR, BACA and Essential Data reports using java (was .Net) and Sybase (was Access DB) and adding MD5 checksum validations to the reports.\nI used java, JSP, Javascript, CSS, Sybase stored procedures, Jboss, Unix shell scripts, Apache IO, SQR and other technologies. I also provide production supports to these financial applications.\n\nWeb.com –  Herndon, VA\t\t\t  \t\t\t\t\t06/2017 – 12/2019\nSenior Java Developer\nWorking in the fulfillment engine team, my major responsibilities are helping team design the architecture of models for e-business work flow, developing new functionalities of company's shopping website using java, jsp, javascript, Restful microservices, SOAP webservices, oralce, sql server, glassfish, tomcat, Spring, Hibernate, Jenkins and other technologies. I also provide 3rd level support to production issues and mentor new team members to get familiar with the procedures and technologies we use.\n\nConcept Solutions Inc. –  Reston, VA \t  \t\t\t\t\t12/2016 – 06/2017\nDOT FAA - Software Engineer\nAs a DOT FAA consultant, I’m working on FNS applications, which include Origination, Management and Distribution of NATAM (Notice to Airmen) information. I’m responsible for developing and supporting NDS and NOS SOAP Web Services. I also take care of new release deployment.\nSkills: Java,  Javascript, Postgres database 9.5, Tomcat 7, Eclipse Neon, etc \n\nUnanet Inc. –  Dulles, VA\t\t\t  \t\t\t\t\t12/2012 – 12/2016\nUnanet software - Senior Java Developer\nUnanet software helps organizations plan, track and manage people and projects. Unanet software provides expense reports, resource planning, project management, accounting, billing and invoicing, vendor payment, customer payment, financial and accounting management, and more than 100 types of reporting features.\n\nI’m responsible for developing new financial features of Unanet 10.0, including but not limited to Vendor management, customer and deposit posting and unposting, journal entry and general ledger management, labor post, etc. \nSkills: Java, JSP, Javascript, YUI, Ajax, CSS, Oracle 12, Sql Server 2012, Angular 2,  Restful microservices, Spring boot, XML, Json, Eclipse Kelper, etc \n\nScolerTec – Washington DC\t\t\t\t  \t\t\t9/2011 – 11/2012\nU.S. Court Consultant - Senior Java Developer\nDistrict CMECF/CVB application\nThe Case Management/Electronic Case Filing (CM/ECF) system is the Federal Judiciary's comprehensive case management system for all bankruptcy, district and appellate courts. CM/ECF allows courts to accept filings and provide access to filed documents over the Internet.\n\nI’m responsible for developing and supporting district CVB component of CM/ECF. \nSkills: JSF, Richfaces, Java, JSP, SOAP web services, Spring, Hibernate, Javascript,  etc \n\nActioNet –  Washingon DC\t\t\t\t  \t\t\t11/2010 – 9/2011\nU.S. Department of Transportation Consultant - Senior Java Developer\nDOT MARAD Credit Program Portfolio Management System (CPPMS)\nThis credit program provides a full faith and credit guarantee by the U.S. Government of debt obligations issued by U.S. or foreign ship owners for the purpose of financing or refinancing either U.S. flag vessels or eligible export vessels constructed, reconstructed, or reconditioned in U.S. shipyards \n\nI was responsible for developing and supporting MARAD CPPMS application. \nSkills: JSF, Java, Seam, Hibernate, EJB, JavaScript, Struts, Oracle 10g, etc\n\n\nPricewaterhouseCoopers - Washington, DC\t\t\t\t\t  07/2006 – 11/2010\nSenior Java developer\neAdvisor\neAdvisor is PwC's online employee financial education and counseling web site that provides users with comprehensive financial counseling. It is a Java based tax application for partnerships calculation of the value of Tax, Debt, depreciation allocations of fixed assets, based on partnership structure. I'm responsible for the design, development, implementation and technical support of eAdvisor.\nSkills used:  Java, JSP, JavaScript, Oracle 10g database, JSF tag library, J2EE, Unix script, etc\nWash Sales application \nWash Sales is a client-server application to collect fund and security data, calculate wash sales and generate deferral and reversal reports for end users. \n\nFor the purposes of IRS Section 1091, a WASH SALE occurs when:\n A loss is realized upon the sale or disposition of stock or securities, and\n The taxpayer has either acquired “substantially identical” securities or entered into a contract or option to acquire substantially identical securities within 30 days before the date of sale or 30 days after the date of sale.\n\nResponsibilities:\nTroubleshooting technical issues, including VB, Java, Excel and db scripts issues.\nUsing Monarch to transform client data into designated template; Validating data using Access tool; Importing data using Wash Sales application; Calculating Wash Sales for client\nGenerating Deferral and Reversal reports for end users. \nSkills: Java, stored procedures, Access, Oracle 10g database.\nK-1 Web\nK1-Web is a web based application which allows clients to upload partnership K1 tax files in batch mode, then categorize and add user security checks when partners download their corresponding K1 files. I'm responsible for developing, setting up this application in UAT, Stage and Production environments, troubleshooting technical issues, helping client upload K1 files and partnership data to database when necessary.\nSkills:  Java, JSP, JavaScript, XML, HTML, SQL Server 2000.\neLKE web application\nThe eLKE system uses automated algorithms to select assets from the client portfolios and combines them according to the rules of Section 1031 to create like-kind exchanges.\n\nMy job is to design, develop, set up this application, troubleshoot code bugs and help practice to load client's data and generate reports.\nSkills: Java, JSP,  Apache tomcat, Oracle 10\nCostSeg\nCostSeg application helps client to identify and segregate assets associated with new construction or construction rehabilitation which result in substantial tax benefits as a result of the attribution of shorter depreciation recovery periods. The services performed include site inspections, cost analysis, engineering takeoffs and the application of indirect construction costs to specific assets. This application is based on the IRS tax revenue procedure 87-56 and code section 1245 and 1250.\n\nResponsibilities: \nDeveloping the application, troubleshooting code issues.\nSkills: VBA, MS Access, SQL Server 2000, Excel programming\n\n \n\nObjectiva Software Solutions - Beijing, China\t\t\t             07/2000 – 04/2003\nSoftware Engineer\n xPression Project\nxPression® is a suite of applications you can use to design, manage and publish customized documents in high volume. \nI was mainly responsible for:\nDesigning, developing and technically supporting xPression Response application. \nDesigning, developing and supporting xPression Framework® for Java application. \nSkills: Java, EJB, JSP, Servlet, JavaScript, XML, HTML, SQLServer2000, Oracle 9i, DB2.\n\nHoffman OLAP application\nHoffman is a web-based OLAP application used by the paper-making manufactories. I was responsible for designing and developing this application with my co-workers.\nSkills: JSP,  JavaScript, Java, XML, HTML, SQL Server.\n \n\nEducation\nMS, University of California Irvine, CA  \t\t\t\t\t09/22/2003 - 03/24/2005\nMajor: Information & Computer Science\nBS, Peking University, Beijing (China)  \t\t\t\t\t09/01/1995 - 07/31/1999\nMajor: Computer Science\n\nPrize & Certification received\n“Sun Java 2 Platform Programmer Certificate”\t\t\t\t02/2002"
# Function to get word positions

# Function to get word positions and extract name, email, and phone number positions
import re
import spacy

# Assuming you have a pre-trained spaCy model loaded
nlp = spacy.load("en_core_web_sm")

# Example skill array (can be replaced with your list)


def get_word_positions(text):
    doc = nlp(text)
    word_positions = []

    # Extract named entities (e.g., name, email, phone) using spaCy
    for ent in doc.ents:
        entity = ""
        # Check if the entity is one of PERSON, ORG, EMAIL, or PHONE
        if ent.label_ in ["PERSON", "ORG", "EMAIL", "PHONE"]:
            # Check if the entity text matches any skill from the skill_array (case insensitive)
            if ent.text.lower() in [skill.lower() for skill in skill_array]:
                entity = "SKILLS"
                ent.label_ = "SKILLS"  # Change the label to "SKILLS" for skills matching
            if ent.text.lower() in [role.lower() for role in roles_array]:
                entity = "ROLE"
                ent.label_ = "ROLE"  # Change the label to "ROLE" for role matching

            
            word_positions.append({
                "label": ent.label_,
                "start": ent.start_char,  # Start position of the entity
                "end": ent.end_char,  # End position of the entity
                "word": ent.text,  # The entity text itself
                "entity": entity if entity else ent.label_  # If it's not a skill, return the original entity
            })

    # Custom handling for emails and phone numbers using regex
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(\+?\d{1,4}[ -]?)?(\(?\d{1,4}\)?[ -]?)?\d{1,4}[ -]?\d{1,4}[ -]?\d{1,4}'

    # Find all emails using regex
    emails = re.finditer(email_pattern, text)
    for email in emails:
        word_positions.append({
            "label": "EMAIL",
            "start": email.start(),
            "end": email.end(),
            "word": email.group(),
            "entity": "EMAIL"
        })

    # Find all phone numbers using regex
    phone_numbers = re.finditer(phone_pattern, text)
    for phone in phone_numbers:
        if(len(phone.group()) >5):
            word_positions.append({
                "label": "PHONE",
                "start": phone.start(),
                "end": phone.end(),
                "word": phone.group(),
                "entity": "PHONE"
            })

    return word_positions

# Test the function
text = resume_text

# Get word positions
word_positions = get_word_positions(text)
for position in word_positions:
    print(position)
# Call the function to get word positions
word_positions = get_word_positions(resume_text)

# Print the word positions
for word in word_positions:
    print(word)