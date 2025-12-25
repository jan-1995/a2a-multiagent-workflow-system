from dotenv import load_dotenv
from google import genai
import os

# Load variables from host_agent/.env
load_dotenv()

key = os.getenv("GOOGLE_API_KEY")
assert key, "GOOGLE_API_KEY is missing in .env"

client = genai.Client(api_key=key)
resp = client.models.generate_content(
    model="gemini-1.5-pro",
    contents="Say 'Hello from Gemini!'"
)

print(resp.text)