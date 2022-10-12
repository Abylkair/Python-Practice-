from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
 return {"message": "Hello it's practice work week7!"}
@app.get("/about")
def about():
 return {"message": "basic website"}