import uvicorn as uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/dummy")
def get_string() -> str:
    return "dummy"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
