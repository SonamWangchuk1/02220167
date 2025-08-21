import json
from jsonschema import validate,ValidationError

FILENAME = "books.json"

# Read
with open(FILENAME, "r") as f:
        data = json.load(f)
    

schema = {
  "type": "object",
  "properties": {
    "Books": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Title": { "type": "string" },
          "Author": { "type": "string" },
          "Genre": { "type": "string" }
        },
        "required": ["Title", "Author", "Genre"]
      }
    }
  },
  "required": ["Books"]
}

try:
    validate(instance= data, schema=schema)
    print(" JSON is valid according to the schema.")
except ValidationError as e:
    print(" JSON validation error:")
    print(e)