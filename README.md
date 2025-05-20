# layout-parser-service
curl -X POST "http://localhost:8000/parse/DBAR/DEMOGRAPHIC/v1" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"John      Smith     123 Main St            5551234567\"}"