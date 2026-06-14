class InterviewAgent:

    def generate(self, career):

        interview_db = {

            # IT
            "Python Developer": [
                "What is Python?",
                "Explain OOP.",
                "What is Flask?",
                "What are decorators?",
                "What is multithreading?"
            ],

            "Java Developer": [
                "What is JVM?",
                "Difference between JDK and JRE?",
                "Explain OOP.",
                "What is Spring Boot?"
            ],

            "AI Engineer": [
                "What is Machine Learning?",
                "What is Deep Learning?",
                "Explain Neural Networks.",
                "What is TensorFlow?"
            ],

            "Cyber Security Analyst": [
                "What is SQL Injection?",
                "What is XSS?",
                "What is a Firewall?",
                "Explain OWASP Top 10."
            ],

            # MBA
            "Marketing Manager": [
                "What is SWOT Analysis?",
                "What is Market Segmentation?",
                "How do you increase brand awareness?"
            ],

            "HR Manager": [
                "How do you resolve conflicts?",
                "Explain recruitment process.",
                "How do you retain employees?"
            ],

            "Financial Analyst": [
                "What is ROI?",
                "What is NPV?",
                "How do you evaluate investments?"
            ],

            # Medical
            "Doctor": [
                "Why did you choose medicine?",
                "How do you handle emergency cases?",
                "What is patient confidentiality?"
            ],

            "Surgeon": [
                "What surgical procedures are you experienced with?",
                "How do you manage operation risks?"
            ],

            "Nurse": [
                "How do you care for critical patients?",
                "How do you handle stress?"
            ],

            # Pharma
            "Pharmacist": [
                "Explain drug interactions.",
                "What is dosage calculation?",
                "How do you prevent medication errors?"
            ],

            # Engineering
            "Mechanical Engineer": [
                "What is Thermodynamics?",
                "Explain IC Engine.",
                "What is CAD?"
            ],

            "Civil Engineer": [
                "What is RCC?",
                "Explain surveying.",
                "What is soil testing?"
            ],

            "Electrical Engineer": [
                "What is Ohm's Law?",
                "Explain Transformer.",
                "What is Power Factor?"
            ],

            # Commerce
            "Accountant": [
                "What is a balance sheet?",
                "What is GST?",
                "What is depreciation?"
            ],

            "Chartered Accountant": [
                "Explain auditing.",
                "What is direct tax?",
                "What is indirect tax?"
            ],

            # Law
            "Lawyer": [
                "Why did you choose law?",
                "How do you prepare a case?",
                "What is constitutional law?"
            ],

            # Education
            "Teacher": [
                "How do you engage students?",
                "What is your teaching methodology?"
            ],

            "Professor": [
                "How do you conduct research?",
                "How do you mentor students?"
            ],

            # Agriculture
            "Agricultural Officer": [
                "What are modern farming techniques?",
                "How do you improve crop yield?"
            ],

            # Aviation
            "Commercial Pilot": [
                "Why do you want to become a pilot?",
                "How do you handle emergencies?"
            ],

            # Hotel Management
            "Hotel Manager": [
                "How do you handle customer complaints?",
                "What is hospitality management?"
            ],

            # Media
            "Journalist": [
                "How do you verify news sources?",
                "What is investigative journalism?"
            ],

            # Design
            "UI/UX Designer": [
                "What is user-centered design?",
                "What tools do you use?"
            ],

            # Government
            "IAS Officer": [
                "Why civil services?",
                "Current affairs question.",
                "How would you solve a public issue?"
            ],

            "Police Officer": [
                "Why do you want to join police?",
                "How do you handle law and order situations?"
            ],

            # Sports
            "Sports Coach": [
                "How do you motivate athletes?",
                "How do you design training plans?"
            ]
        }

        return interview_db.get(
            career,
            [
                "Tell me about yourself.",
                "Why should we hire you?",
                "What are your strengths?",
                "What are your weaknesses?",
                "Where do you see yourself in 5 years?"
            ]
        )