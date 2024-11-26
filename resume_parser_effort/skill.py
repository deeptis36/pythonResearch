def extract_skills(text):
    skills_keywords = ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'Machine Learning', 'Data Science']
    skills_keywords = [
    # **Programming Languages**
    "Python", "JavaScript", "Java", "C#", "PHP", "C++", "Ruby", "Swift", "Kotlin", "Go", "Rust", "TypeScript", "R", "Perl", "SQL",
    
    # **Web Development**
    "HTML", "CSS", "JavaScript", "React", "Angular", "Vue.js", "Node.js", "Express", "Laravel", "Django", "Flask", "Ruby on Rails", "WordPress", "Joomla", "Magento",
    
    # **Front-End Frameworks**
    "React", "Vue.js", "Angular", "Svelte", "Bootstrap", "Tailwind CSS", "Foundation", "Material-UI", "Ant Design",
    
    # **Back-End Frameworks**
    "Node.js", "Django", "Flask", "Laravel", "Spring", "ASP.NET", "Express.js", "Ruby on Rails", "Symfony",
    
    # **Mobile Development**
    "Android", "iOS", "React Native", "Flutter", "Swift", "Kotlin", "Xamarin", "Ionic",
    
    # **Database Management**
    "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Oracle", "Microsoft SQL Server", "Redis", "Cassandra", "Firebase", "Elasticsearch",
    
    # **DevOps & Cloud**
    "Docker", "Kubernetes", "AWS", "Google Cloud", "Azure", "Terraform", "CI/CD", "Jenkins", "Ansible", "Nagios", "Prometheus", "Kubernetes",
    
    # **Version Control**
    "Git", "GitHub", "GitLab", "Bitbucket", "SVN", "Mercurial",
    
    # **Software Development Practices**
    "Agile", "Scrum", "Kanban", "Test-Driven Development (TDD)", "Behavior-Driven Development (BDD)", "Continuous Integration/Continuous Delivery (CI/CD)", "Pair Programming", "Code Reviews",
    
    # **Security**
    "OWASP", "SSL/TLS", "Penetration Testing", "Network Security", "Cybersecurity", "Cryptography", "OAuth", "JWT", "Firewalls", "Encryption", "Vulnerability Assessment", "Cloud Security",
    
    # **Data Science & Machine Learning**
    "Machine Learning", "Deep Learning", "Data Mining", "Natural Language Processing (NLP)", "Computer Vision", "TensorFlow", "Keras", "Scikit-learn", "PyTorch", "Pandas", "NumPy", "Matplotlib", "Seaborn", "SciPy",
    
    # **Data Engineering & Big Data**
    "Hadoop", "Spark", "Kafka", "ETL", "Data Warehousing", "Apache Airflow", "Google BigQuery", "Redshift", "Data Lakes",
    
    # **Business Intelligence & Analytics**
    "Power BI", "Tableau", "Google Analytics", "Excel", "Looker", "Qlik",
    
    # **Networking & Servers**
    "TCP/IP", "DNS", "HTTP/HTTPS", "VPN", "Load Balancing", "Web Servers", "Apache", "NGINX", "Linux", "Windows Server",
    
    # **UI/UX Design**
    "Figma", "Adobe XD", "Sketch", "InVision", "Wireframing", "Prototyping", "User Research", "Usability Testing", "Responsive Design", "Design Systems",
    
    # **Automation & Testing**
    "Selenium", "JUnit", "Cucumber", "Jest", "Mocha", "Chai", "JUnit", "TestNG", "Cypress", "Postman", "SoapUI", "Appium", "JUnit", "Mockito",
    
    # **Artificial Intelligence**
    "Neural Networks", "Reinforcement Learning", "AI Ethics", "Generative AI", "Recurrent Neural Networks (RNN)", "Convolutional Neural Networks (CNN)",
    
    # **Blockchain & Cryptocurrency**
    "Ethereum", "Smart Contracts", "Solidity", "Bitcoin", "Blockchain Development", "DeFi", "NFTs", "Cryptography",
    
    # **AR/VR Development**
    "Unity", "Unreal Engine", "Augmented Reality (AR)", "Virtual Reality (VR)", "Mixed Reality (MR)",
    
    # **Game Development**
    "Unity 3D", "Unreal Engine", "Game Design", "3D Modeling", "Game Physics", "Multiplayer Game Development", "Game AI",
    
    # **Robotics**
    "ROS (Robot Operating System)", "Robotics Simulation", "Sensor Integration", "Autonomous Vehicles",
    
    # **IoT (Internet of Things)**
    "Raspberry Pi", "Arduino", "IoT Protocols", "Sensors", "MQTT", "Bluetooth Low Energy (BLE)",
    
    # **API Development & Integration**
    "RESTful APIs", "GraphQL", "Swagger", "Postman", "OAuth 2.0", "SOAP",
    
    # **Content Management Systems**
    "WordPress", "Joomla", "Drupal", "Magento", "Shopify", "Contentful",
    
    # **SEO & Digital Marketing**
    "Search Engine Optimization (SEO)", "Google Analytics", "Content Marketing", "PPC Campaigns", "Keyword Research", "Social Media Marketing", "Email Marketing",
    
    # **Customer Relationship Management (CRM)**
    "Salesforce", "HubSpot", "Zoho CRM", "Microsoft Dynamics",
    
    # **Project Management Tools**
    "Jira", "Trello", "Asana", "Monday.com", "Basecamp", "Confluence", "ClickUp",
    
    # **Product Management**
    "Roadmap Creation", "Market Research", "User Stories", "Product Lifecycle", "A/B Testing", "Customer Feedback Analysis",
    
    # **Soft Skills**
    "Communication", "Teamwork", "Leadership", "Problem-Solving", "Critical Thinking", "Adaptability", "Creativity", "Time Management", "Collaboration", "Conflict Resolution", "Emotional Intelligence", "Decision-Making", "Project Management", "Negotiation", "Public Speaking", "Presentation Skills", "Customer Service", "Networking",
    
    # **Language Skills**
    "English", "Spanish", "French", "German", "Mandarin", "Hindi", "Arabic", "Italian", "Portuguese", "Russian", "Japanese", "Korean",
    
    # **Other Miscellaneous Skills**
    "Sales", "Marketing", "Human Resources", "Financial Analysis", "Legal Compliance", "Business Development", "Negotiation", "Event Planning", "Research", "Education & Training", "Writing", "Graphic Design", "Photography", "Video Editing", "Podcasting", "Public Relations"
]

    skills = []
    for skill in skills_keywords:
        if skill.lower() in text.lower():
            skills.append(skill)
    return skills