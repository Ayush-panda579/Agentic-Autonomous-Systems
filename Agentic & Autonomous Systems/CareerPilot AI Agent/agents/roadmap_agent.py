class RoadmapAgent:

    def generate(self, career):

        roadmap = {

            "Python Developer": [
                "Python Basics",
                "OOP",
                "Flask/Django",
                "SQL",
                "REST APIs",
                "Projects",
                "Deployment"
            ],

            "Java Developer": [
                "Java Basics",
                "OOP",
                "Collections",
                "JDBC",
                "Spring Boot",
                "Microservices",
                "Projects"
            ],

            "Web Developer": [
                "HTML",
                "CSS",
                "JavaScript",
                "Bootstrap",
                "React",
                "Backend Development",
                "Projects"
            ],

            "Full Stack Developer": [
                "Frontend",
                "Backend",
                "Database",
                "REST APIs",
                "Authentication",
                "Deployment",
                "Projects"
            ],

            "Data Analyst": [
                "Excel",
                "SQL",
                "Python",
                "Pandas",
                "Statistics",
                "Power BI",
                "Projects"
            ],

            "Data Scientist": [
                "Python",
                "Statistics",
                "Machine Learning",
                "Deep Learning",
                "NLP",
                "MLOps",
                "Projects"
            ],

            "AI Engineer": [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "TensorFlow",
                "PyTorch",
                "LLMs",
                "AI Projects"
            ],

            "Cyber Security Analyst": [
                "Networking",
                "Linux",
                "Security Fundamentals",
                "Ethical Hacking",
                "Penetration Testing",
                "SIEM",
                "Security Projects"
            ],

            "Cloud Engineer": [
                "Linux",
                "Networking",
                "AWS",
                "Azure",
                "Docker",
                "Kubernetes",
                "Cloud Projects"
            ],

            "DevOps Engineer": [
                "Linux",
                "Git",
                "Docker",
                "Kubernetes",
                "CI/CD",
                "Jenkins",
                "Cloud"
            ],

            "MBA Marketing": [
                "Marketing Fundamentals",
                "Consumer Behavior",
                "Digital Marketing",
                "SEO",
                "SEM",
                "Analytics",
                "Marketing Projects"
            ],

            "MBA Finance": [
                "Accounting",
                "Financial Analysis",
                "Investment Banking",
                "Risk Management",
                "Equity Research",
                "Financial Modeling"
            ],

            "MBA HR": [
                "Recruitment",
                "Employee Relations",
                "Payroll",
                "Performance Management",
                "HR Analytics",
                "Labor Laws"
            ],

            "Business Analyst": [
                "Business Analysis",
                "Requirements Gathering",
                "SQL",
                "Excel",
                "Power BI",
                "Agile",
                "Projects"
            ],

            "Doctor": [
                "MBBS",
                "Clinical Training",
                "Internship",
                "Residency",
                "Specialization",
                "Medical Practice"
            ],

            "Surgeon": [
                "MBBS",
                "MS",
                "Surgical Training",
                "Residency",
                "Specialization",
                "Practice"
            ],

            "Pharmacist": [
                "Pharmacology",
                "Drug Formulation",
                "Clinical Pharmacy",
                "Quality Control",
                "Regulatory Affairs"
            ],

            "Clinical Research Associate": [
                "Clinical Trials",
                "Drug Development",
                "Research Methodology",
                "Regulations",
                "Documentation"
            ],

            "Lawyer": [
                "LLB",
                "Legal Research",
                "Drafting",
                "Litigation",
                "Court Practice",
                "Specialization"
            ],

            "Corporate Lawyer": [
                "Corporate Law",
                "Contracts",
                "Compliance",
                "Mergers & Acquisitions",
                "Legal Practice"
            ],

            "Chartered Accountant": [
                "Accounting",
                "Taxation",
                "Auditing",
                "Corporate Law",
                "Financial Reporting"
            ],

            "Investment Banker": [
                "Finance",
                "Valuation",
                "Financial Modeling",
                "Mergers",
                "Capital Markets"
            ],

            "Graphic Designer": [
                "Photoshop",
                "Illustrator",
                "Typography",
                "Branding",
                "Portfolio Building"
            ],

            "UI/UX Designer": [
                "Design Principles",
                "Figma",
                "Wireframing",
                "Prototyping",
                "User Research",
                "Portfolio"
            ],

            "Agriculture Officer": [
                "Agronomy",
                "Soil Science",
                "Crop Management",
                "Irrigation",
                "Agricultural Technology"
            ],

            "Teacher": [
                "Subject Expertise",
                "Teaching Methods",
                "Lesson Planning",
                "Classroom Management",
                "Assessment"
            ],

            "Government Officer": [
                "General Knowledge",
                "Current Affairs",
                "Reasoning",
                "Aptitude",
                "Polity",
                "Mock Tests"
            ]
        }

        return roadmap.get(
            career,
            [
                "Domain Fundamentals",
                "Skill Development",
                "Projects",
                "Internships",
                "Certifications",
                "Interview Preparation"
            ]
        )