import os

import uvicorn
from fastapi import FastAPI

var = os.getenv("SYSTEM_PROMPT", "NOT PROVIDED!!!!!")
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the simple HTTP service"}


if __name__ == "__main__":
    print(f"Staring symple service with SYSTEM_PROMPT={var}")
    uvicorn.run(app, host="0.0.0.0", port=8181)
