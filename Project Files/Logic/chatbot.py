from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

creds = Credentials(api_key="cjhxM8OWLyjtVflsSDuTDb4TycWNRYAl3xMkcHbuuFq4", url="https://us-south.ml.cloud.ibm.com")

model = ModelInference(
    model_id="ibm/granite-3-8b-instruct",
    credentials=creds,
    project_id="245d62b5-7b2f-477f-8bf1-ece30f3fa579"
)

def generate_feedback_response(user_input: str) -> str:
    prompt = f"Citizen complaint: {user_input}\nResponse:"
    res = model.generate_text(prompt=prompt)
    return res


