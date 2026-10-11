from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

interaction = client.interactions.create(
    model = "gemini-3.8-flash",
    input = "who is called the father of the nation in India"
)

print(interaction.output_text)
