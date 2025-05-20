from fastapi import FastAPI, HTTPException, Body
from parser.layout_loader import load_layout
from pydantic import BaseModel
import logging

app = FastAPI()

class ParseRequest(BaseModel):
    text: str

@app.post("/parse/{source_system}/{layout_key}/v{version}")
async def parse_text(
    source_system: str,
    layout_key: str,
    version: str,
    payload: ParseRequest = Body(...)
):
    logging.info(f"Parsing text: {payload.text}")
    freeform_text = payload.text
    layout = load_layout(source_system, layout_key, version)

    parsed = {}
    for field in layout:
        start = field["start"]
        length = field["length"]
        end = start + length
        parsed[field["name"]] = freeform_text[start:end].strip()

    return {"parsed_data": parsed}
