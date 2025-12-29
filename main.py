from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "我在雲端寫程式！"}
#下載requirement.txt