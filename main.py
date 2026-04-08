from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print("Ktoś wywołał endpoint /")
    return {"message": "App Platform k8s!"}