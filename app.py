from google import genai
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("API_KEY not found. Add it to your .env file.")

client = genai.Client(api_key=api_key)
MODEL = "gemini-3.8-flash"

def get_response(query):
    try:
        interaction = client.interactions.create(model=MODEL, input=query)
        return interaction.output_text, None
    except Exception as e:
        app.logger.error("Gemini call failed: %s", e)
        return None, "Something went wrong. Please try again."

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    query = (request.form.get("query") or "").strip()
    if not query:
        return render_template("index.html", error="Please type a question."), 400

    response, error = get_response(query)
    return render_template("result.html", query=query, response=response, error=error)

if __name__ == "__main__":
    app.run(debug=True)
