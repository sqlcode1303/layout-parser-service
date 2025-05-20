# layout-parser-service
variable layout
curl -X POST "http://127.0.0.1:8000/parse" \
  -H "Content-Type: application/json" \
  -d '{
        "source_system": "DBAR",
        "layout_key": "DEMOGRAPHIC",
        "version": "1.0",
        "text": "John      Smith     123 Main St, City         1234567890"
      }'
