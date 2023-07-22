from fastapi import FastAPI
import random

app = FastAPI()

smileys = ["^_^", "~_~", "o.o", "O.o"]

@app.get("/")
async def get_smiley():
    random_smiley = random.choice(smileys)
    return {"smiley": random_smiley}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

