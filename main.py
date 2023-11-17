from typing import Any

import uvicorn
from fastapi import FastAPI, Request

from database import prepare_db, find_matching_template
from services import get_field_types

app = FastAPI()


@app.post("/get_form")
async def get_form(request: Request) -> dict[str, Any]:
    data_types = get_field_types(dict(request.query_params))
    if matching_template := find_matching_template(data_types):
        return {"form_name": matching_template}
    else:
        return data_types


if __name__ == "__main__":
    prepare_db()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
