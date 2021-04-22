import uvicorn
from fastapi import FastAPI
from src.routes import api_router
from dotenv import dotenv_values

app = FastAPI()
config = dotenv_values(".env")
app.include_router(api_router, prefix=config["PREFIX"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
