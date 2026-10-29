from fastapi import FastAPI

app = FastAPI(title="Microservicio DevOps Eval2")

@app.get("/")
def read_root():
    return {"message": "Hola desde el microservicio DevOps", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "ok"}