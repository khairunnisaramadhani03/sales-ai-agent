import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def ask_groq(prompt, model="llama-3.1-8b-instant"):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    res = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return res.choices[0].message["content"]
