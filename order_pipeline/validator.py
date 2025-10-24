import re
from typing import Any


class Validator:
    REQUIRED = ['order_id', 'timestamp', 'item', 'quantity', 'price', 'total', 'payment_status']
    QPT = ['quantity', 'price', 'total']

    def validate_one(self, row: dict[str, Any]) -> dict[str, Any] | None:
        for field in self.REQUIRED:
            if field in row:
                row[field] = str(row[field])
            if field not in row or row[field] == '':
                return None
        for field in self.QPT:
            
            if not re.search(r'[0-9]+', row[field]) or re.match(r'^-', row[field]):
                return None
        return row
        
    
    def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        validated_data: list[dict[str, Any]] = []
        for row in data:
            result = self.validate_one(row)
            if result:
                validated_data.append(row)
        return validated_data
        
        
        
        
