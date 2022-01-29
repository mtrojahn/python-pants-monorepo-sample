import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from libs.converters.etl import convert_to_string

app = FastAPI()


class DefaultResult(BaseModel):
    message: str


@app.get("/")
def get_string(number: int) -> DefaultResult:
    return DefaultResult(message=convert_to_string(number))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
