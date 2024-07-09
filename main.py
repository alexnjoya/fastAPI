from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hope you are doing something good today "}

@app.post("/createPost")
def createPost():
    return {"message": "creating a new post"}