# list_models.py
from google import genai
import config

client = genai.Client(api_key=config.API_KEY)

print("Checking available models...\n")
for m in client.models.list():
    # Only show models supporting text generation
    if "generateContent" in m.supported_actions:
        print(f"Model ID: {m.name}")
        