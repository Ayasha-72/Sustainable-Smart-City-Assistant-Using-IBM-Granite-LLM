import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

creds = Credentials(
    api_key=os.getenv("WATSONX_API_KEY"),
    url=os.getenv("WATSONX_URL")
)

model = ModelInference(
    model_id="ibm/granite-3-8b-instruct",
    credentials=creds,
    project_id=os.getenv("WATSONX_PROJECT_ID")
)

def generate_feedback_response(user_input: str) -> str:
    prompt = f"Citizen complaint: {user_input}\nResponse:"
    response = model.generate_text(prompt=prompt)
    return response



