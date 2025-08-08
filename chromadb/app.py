import chromadb
import chromadb.config
from chromadb.server.fastapi import import FastAPI

settings = chromadb.config.Settings()
server = FastAPI(settings)
app = server.app()

@app.get("/")
def root():
    return {"status": "ok"}
