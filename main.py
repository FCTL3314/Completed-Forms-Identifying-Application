import uvicorn
from fastapi import FastAPI, Request

from database import prepare_db
from services import get_form_service

app = FastAPI()


@app.post("/get_form", name="get_form")
async def get_form(request: Request) -> dict[str, str]:
    return get_form_service(dict(request.query_params))


if __name__ == "__main__":
    prepare_db()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
