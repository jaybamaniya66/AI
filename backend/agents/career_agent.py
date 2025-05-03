from agents.base_agent import BaseAgent

class CarrerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name = "carrer agent",
            description = "This agent will tell you the carrer aspects of the portfolio"
        )
        self.skills = {
            "language" : ["pyhton", "java"],
            "framework": ["react", "angular"]
        },
        self.experience = [
            {
                "title": "Senior full stack developer",
                "company": "upvision",
                "period" : 22,
                "res": ["qa", "development", "devops"]
            },
            {
                "title": "Senior full stack developer",
                "company": "upvision",
                "period" : 22,
                "res": ["qa", "development", "devops"]
            },
        ]

    def get_skill_summary(self):
        prompt = f"""
        Generate a professional summary for the portfolio website:

        Programming Language: {', '.join(self.skills['language'])}
        Framework & Libraries: {', '.join(self.skills['framework'])}

        """

        return self.get_response(prompt)
        

    def get_experience_summary(self):
        experience_text = "Work experience\n\n"

        for ex in self.experience():
            experience_text += f"## job {ex['title']} at {ex['company']}\n"
            for response in ex['res']:
                experience_text += f" responsiblities for the role is {response}\n"



        prompt = f"""
            Based on the experience give me the experience summary for the portfolio website:
            {experience_text}

            Highlight career progression, key achievements, and growth. Format the response in markdown.
        """
        return self.get_response(prompt)
    
    def access_job_title(self, job_description):
        added_skills = []
        for trial,value in enumerate(self.skills()):
            added_skills.extend(value)

        prompt = f"""
            Access the job fit based on the skills and job descriptions:

            Skills: 
            {added_skills}

            job_description:
            {job_description}

            Provide an analysis of strengths, potential gaps, and overall suitability for the role. Format the response in markdown.

        """


        return self.get_response(prompt)