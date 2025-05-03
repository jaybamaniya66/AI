from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import json
import requests
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

class BaseAgent:
    def __init__(self,name, description):
        self.name = name,
        self.description = description

        self.api_key = os.getenv("GROQ_TOKEN")

        def search_web(self,query):
            try: 
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }

                data = {
                    "model": "llama3-8b-8192",
                    "message": [
                        {
                            "role": "system",
                            "content": f"you are {self.name} with {self.description}. Response in good and concise manner for the following Information"
                        },
                        {
                            "role": "user",
                            "content": query
                        }
                    ],
                    "temperature": 0.7,
                    "max_token": 500
                }

                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers=headers,
                    json=data
                )

                if response.status_code == 200:
                    return response.json()["choices"][0]["message"]["content"]
                else:
                    return f"Error: {response.status_code} - {response.text}"

            except Exception as e:
                return f"An error occured with: {str(e)}"

class WelcomeAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name = "Welcome Agent"
            description="a weclome agent will introduce everything in the professional portfolio"
        )
    def greet(self, visitor_type=None):
            if visitor_type == "employer":
                return self.get_response("Generate a warm welcome message for an employer visiting a programmer's portfolio website. Suggest they check out the Projects and Career sections.")
            elif visitor_type == "client":
                return self.get_response("Generate a warm welcome message for a potential client visiting a programmer's portfolio website. Suggest they check out the Services section.")
            elif visitor_type == "fellow_programmer":
                return self.get_response("Generate a warm welcome message for a fellow programmer visiting a programmer's portfolio website. Suggest they check out the Projects and Research sections.")
            else:
                return self.get_response("Generate a general welcome message for a visitor to a programmer's portfolio website. Ask if they are an employer, client, or fellow programmer.")

    def suggest_section(self, interest):
        return self.get_response(f"A visitor to my portfolio website has expressed interest in {interest}. Suggest which section(s) of the website they should visit based on this interest.")

    
base_agent = BaseAgent()
welcome_agent = WelcomeAgent()

@app.route('/api/welcome', methods=['POST'])
def welcome_agent_point():
    pass