import json
from typing import Any

class Reader:
   
    def read(self) -> list[dict[str, Any]]:
        try:
            with open('shoplink.json', 'r') as file:
                content: list[dict[str, Any]] = json.load(file)
                return content
        except json.JSONDecodeError:
            raise ValueError('File is empty or invalid')


#print(Reader().read('shoplink.json')[:2])           