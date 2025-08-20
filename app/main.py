from fastapi import FastAPI

app = FastAPI(title="DevOps FastAPI Capstone")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI CI/CD Capstone 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}
