from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Bienvenido a FastAPI"}