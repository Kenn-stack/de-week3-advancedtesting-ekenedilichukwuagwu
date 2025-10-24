import json
from typing import Any

class Exporter:
    
    def export_to_json_file(self, transformed_data: list[dict[str, Any]]):
        with open('shoplink_cleaned.json', 'w') as file:
            json.dump(transformed_data, file)