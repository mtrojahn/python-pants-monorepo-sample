import uvicorn as uvicorn
from fastapi import FastAPI
from libs.converters.etl import convert_to_string

app = FastAPI()


@app.get("/")
def get_string(number: int):
    return {"result": convert_to_string(number)}


if __name__ == "__main__":
    uvicorn.run(app)
