import asyncio
import cognee

memories = [
    "Dad always said never sign a contract without sleeping on it. A deal that cannot wait until morning is not a deal worth making.",
    "He believed that the two most important days in a person's life are the day you are born and the day you find out why.",
    "Dad used to say that money is a terrible master but an excellent servant. Never let it run your life.",
    "He always told me to apologize when I am wrong, but to stand firm when I know I am right. Knowing the difference is wisdom.",
    "Dad said the best thing a father can do for his children is to love their mother. Everything else follows from that.",
    "He believed in waking up early. He said the morning hours belong to you before the world takes them.",
    "Dad never trusted people who were rude to waiters. He said how you treat people who cannot do anything for you reveals your true character.",
    "He always said read more than you talk. You already know what you know. Books teach you what you do not.",
    "Dad told me that failure is not falling down. Failure is refusing to get back up.",
    "He said the most expensive thing in the world is a closed mind. Keep yours open no matter the cost.",
]

async def load():
    print("Loading demo memories...")
    for i, memory in enumerate(memories):
        await cognee.remember(memory)
        print(f"Remembered {i+1}/{len(memories)}: {memory[:60]}...")
    print("Done. All memories loaded.")

asyncio.run(load())