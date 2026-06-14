from agents.resume_agent import ResumeAgent
from agents.career_agent import CareerAgent
from agents.skill_gap_agent import SkillGapAgent
from agents.roadmap_agent import RoadmapAgent
from agents.interview_agent import InterviewAgent


class OrchestratorAgent:

    def __init__(self):

        self.resume = ResumeAgent()
        self.career = CareerAgent()
        self.gap = SkillGapAgent()
        self.roadmap = RoadmapAgent()
        self.interview = InterviewAgent()

    def process_resume(self, text):

        # Extract skills
        skills = self.resume.analyze(text)

        # Career recommendations
        careers = self.career.recommend(skills)

        # Skill gaps
        gaps = self.gap.find_gap(skills)

        # Roadmaps for each career
        roadmaps = {}

        for career in careers:
            roadmaps[career] = self.roadmap.generate(career)

        # Interview questions for each career
        interview_questions = {}

        for career in careers:
            interview_questions[career] = (
                self.interview.generate(career)
            )

        return {

            "skills": skills,

            "recommended_careers": careers,

            "skill_gaps": gaps,

            "roadmaps": roadmaps,

            "interview_questions":
                interview_questions
        }