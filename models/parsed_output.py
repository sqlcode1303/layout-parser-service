from pydantic import BaseModel
from typing import Dict

class ParsedOutput(BaseModel):
    data: Dict[str, str]
