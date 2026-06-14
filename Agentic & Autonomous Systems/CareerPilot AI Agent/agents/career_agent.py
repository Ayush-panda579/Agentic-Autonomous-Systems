class CareerAgent:

    def recommend(self, skills):

        skills = [s.lower() for s in skills]

        careers = set()

        career_map = {

            # =====================
            # IT & SOFTWARE
            # =====================
            "python": ["Python Developer"],
            "java": ["Java Developer"],
            "react": ["Frontend Developer"],
            "flask": ["Backend Developer"],
            "aws": ["Cloud Engineer"],
            "cybersecurity": ["Cyber Security Analyst"],
            "machine learning": ["AI Engineer"],

            # =====================
            # MEDICAL
            # =====================
            "mbbs": ["Doctor"],
            "medicine": ["Doctor"],
            "surgery": ["Surgeon"],
            "dentist": ["Dental Surgeon"],
            "nursing": ["Nurse"],
            "physiotherapy": ["Physiotherapist"],
            "radiology": ["Radiologist"],
            "pathology": ["Pathologist"],

            # =====================
            # PHARMA
            # =====================
            "pharmacy": ["Pharmacist"],
            "b.pharm": ["Pharmacist"],
            "clinical research": ["Clinical Research Associate"],
            "drug development": ["Pharmaceutical Scientist"],
            "pharmacology": ["Pharmacologist"],

            # =====================
            # MBA / MANAGEMENT
            # =====================
            "marketing": ["Marketing Manager"],
            "finance": ["Financial Analyst"],
            "hr": ["HR Manager"],
            "human resources": ["HR Manager"],
            "operations": ["Operations Manager"],
            "business": ["Business Analyst"],
            "mba": ["Management Consultant"],
            "sales": ["Sales Manager"],

            # =====================
            # COMMERCE
            # =====================
            "accounting": ["Accountant"],
            "tally": ["Accountant"],
            "taxation": ["Tax Consultant"],
            "ca": ["Chartered Accountant"],
            "audit": ["Auditor"],

            # =====================
            # ENGINEERING
            # =====================
            "mechanical": ["Mechanical Engineer"],
            "civil": ["Civil Engineer"],
            "electrical": ["Electrical Engineer"],
            "electronics": ["Electronics Engineer"],
            "automobile": ["Automobile Engineer"],
            "robotics": ["Robotics Engineer"],

            # =====================
            # LAW
            # =====================
            "law": ["Lawyer"],
            "advocate": ["Advocate"],
            "legal": ["Legal Advisor"],
            "corporate law": ["Corporate Lawyer"],

            # =====================
            # EDUCATION
            # =====================
            "teaching": ["Teacher"],
            "education": ["Professor"],
            "research": ["Research Scholar"],
            "phd": ["Research Scientist"],

            # =====================
            # AGRICULTURE
            # =====================
            "agriculture": ["Agricultural Officer"],
            "agronomy": ["Agronomist"],
            "horticulture": ["Horticulture Specialist"],

            # =====================
            # DESIGN
            # =====================
            "figma": ["UI/UX Designer"],
            "photoshop": ["Graphic Designer"],
            "animation": ["Animator"],

            # =====================
            # MEDIA
            # =====================
            "journalism": ["Journalist"],
            "content writing": ["Content Writer"],
            "digital marketing": ["Digital Marketer"],

            # =====================
            # GOVERNMENT
            # =====================
            "upsc": ["IAS Officer"],
            "gpsc": ["State Civil Service Officer"],
            "ssc": ["Government Officer"],
            "banking": ["Bank PO"],
            "railway": ["Railway Officer"],

            # =====================
            # AVIATION
            # =====================
            "pilot": ["Commercial Pilot"],
            "aviation": ["Aviation Manager"],
            "aircraft maintenance": ["Aircraft Engineer"],

            # =====================
            # HOTEL MANAGEMENT
            # =====================
            "hospitality": ["Hotel Manager"],
            "chef": ["Executive Chef"],
            "tourism": ["Tourism Manager"],

            # =====================
            # SPORTS
            # =====================
            "sports": ["Sports Coach"],
            "fitness": ["Fitness Trainer"],
            "nutrition": ["Nutritionist"]
        }

        for skill in skills:

            if skill in career_map:

                careers.update(career_map[skill])

        if not careers:
            careers.add("Career Counselling Required")

        return list(careers)