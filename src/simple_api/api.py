from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def read_root():
    name = os.environ.get('DEV_NAME', "Neo")
    message = f"Hello World, I am {name}!"
    return {"Message": message}
