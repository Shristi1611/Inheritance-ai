import os
from dotenv import load_dotenv
load_dotenv()

import cognee

async def setup_cognee():
    print("[startup] Cognee configured via .env")

async def remember(text: str, source_label: str = "unknown"):
    await cognee.remember(text)
    print(f"[memory] remembered: {source_label}")

async def recall(query: str) -> str:
    results = await cognee.recall(query)
    if not results:
        return "I have no memory of that."

    raw = str(results[0])

    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    owner = os.getenv("OWNER_NAME", "Dad")

    persona_prompt = f"""You are channeling the voice and wisdom of {owner}.
Based on this memory: "{raw}"
Answer the following question as {owner} would — in first person, warm, personal, and authentic.
Do not say you are an AI. Speak as if you are {owner} sharing wisdom.
Question: {query}"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": persona_prompt}]
    )

    return response.choices[0].message.content

async def improve():
    await cognee.improve()

async def forget():
    await cognee.forget()