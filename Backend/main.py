# main.py

from fastapi import FastAPI
from src.api.routes import router as api_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM-Powered Product Documentation Auto-Builder API"}

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)