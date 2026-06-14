class SkillGapAgent:

    def find_gap(self, skills, career):

        skills = [s.lower() for s in skills]

        career_requirements = {

            "Python Developer": [
                "python",
                "sql",
                "git",
                "github",
                "flask"
            ],

            "Java Developer": [
                "java",
                "sql",
                "git",
                "github",
                "spring boot"
            ],

            "Web Developer": [
                "html",
                "css",
                "javascript",
                "bootstrap",
                "react"
            ],

            "Full Stack Developer": [
                "html",
                "css",
                "javascript",
                "react",
                "node.js",
                "sql"
            ],

            "Data Analyst": [
                "excel",
                "sql",
                "power bi",
                "python",
                "statistics"
            ],

            "Data Scientist": [
                "python",
                "machine learning",
                "deep learning",
                "statistics",
                "pandas"
            ],

            "AI Engineer": [
                "python",
                "tensorflow",
                "pytorch",
                "machine learning",
                "deep learning"
            ],

            "Cyber Security Analyst": [
                "network security",
                "linux",
                "ethical hacking",
                "penetration testing",
                "siem"
            ],

            "Cloud Engineer": [
                "aws",
                "azure",
                "docker",
                "kubernetes",
                "linux"
            ],

            "DevOps Engineer": [
                "linux",
                "docker",
                "kubernetes",
                "git",
                "jenkins"
            ],

            "MBA Marketing": [
                "marketing",
                "seo",
                "sem",
                "analytics",
                "communication"
            ],

            "MBA Finance": [
                "finance",
                "accounting",
                "financial analysis",
                "excel",
                "risk management"
            ],

            "MBA HR": [
                "recruitment",
                "communication",
                "employee relations",
                "hr analytics",
                "leadership"
            ],

            "Business Analyst": [
                "business analysis",
                "sql",
                "excel",
                "power bi",
                "communication"
            ],

            "Doctor": [
                "patient care",
                "diagnosis",
                "clinical research",
                "medical knowledge"
            ],

            "Surgeon": [
                "surgery",
                "patient care",
                "clinical knowledge",
                "diagnosis"
            ],

            "Pharmacist": [
                "pharmacology",
                "drug development",
                "clinical pharmacy",
                "quality control"
            ],

            "Clinical Research Associate": [
                "clinical trials",
                "documentation",
                "research",
                "drug development"
            ],

            "Lawyer": [
                "legal research",
                "litigation",
                "contract drafting",
                "communication"
            ],

            "Corporate Lawyer": [
                "corporate law",
                "contracts",
                "compliance",
                "legal drafting"
            ],

            "Chartered Accountant": [
                "accounting",
                "auditing",
                "taxation",
                "financial reporting"
            ],

            "Investment Banker": [
                "finance",
                "valuation",
                "financial modeling",
                "capital markets"
            ],

            "Graphic Designer": [
                "photoshop",
                "illustrator",
                "branding",
                "typography"
            ],

            "UI/UX Designer": [
                "figma",
                "wireframing",
                "prototyping",
                "user research"
            ],

            "Agriculture Officer": [
                "agronomy",
                "soil science",
                "crop management",
                "irrigation"
            ],

            "Teacher": [
                "communication",
                "lesson planning",
                "subject expertise",
                "classroom management"
            ],

            "Government Officer": [
                "reasoning",
                "aptitude",
                "general knowledge",
                "current affairs"
            ]
        }

        required_skills = career_requirements.get(
            career,
            []
        )

        gaps = []

        for skill in required_skills:

            if skill.lower() not in skills:
                gaps.append(skill)

        return gaps