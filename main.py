import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import dotenv

from app.apps_router import main_router

app = FastAPI(title="FastAPI TODO service", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok"}


app.include_router(main_router)

if __name__ == "__main__":
    port = 8080
    if dotenv.load_dotenv():
        port = int(os.environ.get("PORT"))
    uvicorn.run(app, host="0.0.0.0", port=port)
