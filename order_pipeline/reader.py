import json
import re
from typing import Any

class Reader:
   
    def read(self, path: str) -> list[dict[str, Any]]:
        if re.search(r'\.json$', path):
            try:
                with open(path, 'r') as file:
                    content: list[dict[str, Any]] = json.load(file)
                    return content
            except json.JSONDecodeError:
                raise ValueError('File is empty or invalid')
        else:
            raise ValueError('Expected a JSON file')
    

print(Reader().read('shoplink.json')[:2])           