class ResumeAgent:

    def analyze(self, text):

        text = text.lower()

        skills = []

        keywords = {

            # Programming
            "python": "Python",
            "java": "Java",
            "c": "C",
            "c++": "C++",
            "c#": "C#",
            "javascript": "JavaScript",
            "typescript": "TypeScript",
            "php": "PHP",

            # Web Development
            "html": "HTML",
            "css": "CSS",
            "bootstrap": "Bootstrap",
            "react": "React",
            "angular": "Angular",
            "vue": "Vue",
            "node.js": "Node.js",
            "flask": "Flask",
            "django": "Django",

            # Database
            "sql": "SQL",
            "mysql": "MySQL",
            "postgresql": "PostgreSQL",
            "mongodb": "MongoDB",
            "oracle": "Oracle",

            # Cloud
            "aws": "AWS",
            "azure": "Azure",
            "gcp": "Google Cloud",

            # DevOps
            "docker": "Docker",
            "kubernetes": "Kubernetes",
            "jenkins": "Jenkins",
            "git": "Git",
            "github": "GitHub",

            # AI / ML
            "machine learning": "Machine Learning",
            "deep learning": "Deep Learning",
            "tensorflow": "TensorFlow",
            "pytorch": "PyTorch",
            "nlp": "NLP",
            "computer vision": "Computer Vision",

            # Cyber Security
            "penetration testing": "Penetration Testing",
            "ethical hacking": "Ethical Hacking",
            "network security": "Network Security",
            "cryptography": "Cryptography",
            "siem": "SIEM",

            # Data Science
            "pandas": "Pandas",
            "numpy": "NumPy",
            "power bi": "Power BI",
            "tableau": "Tableau",
            "data analysis": "Data Analysis",

            # MBA
            "marketing": "Marketing",
            "sales": "Sales",
            "finance": "Finance",
            "accounting": "Accounting",
            "business analysis": "Business Analysis",
            "operations": "Operations",
            "human resources": "Human Resources",

            # Medical
            "patient care": "Patient Care",
            "diagnosis": "Diagnosis",
            "clinical research": "Clinical Research",
            "surgery": "Surgery",
            "medical coding": "Medical Coding",

            # Pharmacy
            "pharmacology": "Pharmacology",
            "drug development": "Drug Development",
            "clinical pharmacy": "Clinical Pharmacy",
            "quality control": "Quality Control",

            # Law
            "legal research": "Legal Research",
            "litigation": "Litigation",
            "contract drafting": "Contract Drafting",
            "corporate law": "Corporate Law",

            # Design
            "photoshop": "Photoshop",
            "illustrator": "Illustrator",
            "figma": "Figma",
            "ui ux": "UI/UX Design",
            "graphic design": "Graphic Design",

            # Agriculture
            "crop management": "Crop Management",
            "soil science": "Soil Science",
            "agronomy": "Agronomy",
            "irrigation": "Irrigation",

            # Government Exams
            "reasoning": "Reasoning",
            "aptitude": "Aptitude",
            "general knowledge": "General Knowledge",
            "current affairs": "Current Affairs",

            # Soft Skills
            "leadership": "Leadership",
            "communication": "Communication",
            "teamwork": "Teamwork",
            "problem solving": "Problem Solving",
            "critical thinking": "Critical Thinking"
        }

        for keyword, skill in keywords.items():

            if keyword in text:
                skills.append(skill)

        return list(set(skills))