from openai import OpenAI
from schemas import StudyPlan, FashionTip, MoodBooster
import random
import google.generativeai as genai

import google.generativeai as genai


genai.configure(api_key="AIzaSyAe8ksUMxTwZ98I6PD_GFbnY7aQUql4OtY")


client = genai.GenerativeModel("gemini-1.5-flash")


def ask_bestie(message: str, mode: str = "chat"):
    response = client.generate_content(
        message,
        generation_config={
            "temperature": 0.8 if mode == "fun" else 0.3,
            "top_p": 0.9,
        }
    )
    return response.text


if __name__ == "__main__":
    print("💖 AI Bestie is ready! Chat with her below:\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        reply = ask_bestie(user_input, mode="fun")
        print(f"\nBestie: {reply}\n")

