from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from parser.layout_loader import load_layout
from parser.parser import parse_text
from models.parsed_output import ParsedOutput

app = FastAPI()

class ParseRequest(BaseModel):
    source_system: str
    layout_key: str
    version: str = "1.0"
    text: str

@app.post("/parse", response_model=ParsedOutput)
def parse(request: ParseRequest):
    try:
        layout = load_layout(request.source_system, request.layout_key, request.version)
        parsed = parse_text(request.text, layout)
        return {"data": parsed}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
