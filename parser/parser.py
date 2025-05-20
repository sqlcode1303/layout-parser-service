def parse_text(text: str, layout: dict) -> dict:
    result = {}
    for field in layout["fields"]:
        start = field["start"]
        end = start + field["length"]
        value = text[start:end].strip()
        result[field["name"]] = value
    return result
