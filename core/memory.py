import cognee
from core.config import config

async def setup_cognee():
    print("[startup] Cognee configured via .env")

async def remember(text: str, source_label: str = "unknown"):
    await cognee.remember(text)
    print(f"[memory] remembered: {source_label}")

async def recall(query: str) -> str:
    results = await cognee.recall(query)
    if not results:
        return f"{config.OWNER_NAME} left no memory of this."
    
    raw = str(results[0])
    
    from groq import Groq
    client = Groq(api_key=config.GROQ_API_KEY)
    
    persona_prompt = f"""You are channeling the voice and wisdom of {config.OWNER_NAME}.
Based on this memory: "{raw}"
Answer the following question as {config.OWNER_NAME} would — in first person, warm, personal, and authentic.
Do not say you are an AI. Speak as if you are {config.OWNER_NAME} sharing wisdom.
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