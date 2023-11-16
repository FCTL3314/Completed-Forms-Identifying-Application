import uvicorn
from fastapi import FastAPI, Request

from database import prepare_db, find_matching_template
from validators import is_field_valid, infer_field_types

app = FastAPI()


@app.get("/get_form")
async def get_form(request: Request):
    params = dict(request.query_params)
    data_types = infer_field_types(params)
    for field_type, value in zip(data_types.values(), params.values()):
        if not is_field_valid(value, field_type):
            return {field_type: "Validation error"}
    if matching_template := find_matching_template(params):
        return {"form_name": matching_template}
    else:
        return data_types


if __name__ == "__main__":
    prepare_db()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
