import re
from typing import Any
from dateutil import parser


class Transformer:
    QPT: list[str] = ['quantity', 'price', 'total']

    
    def to_numeric(self, val: str, kind: str) -> int | float | None:
        digits = re.search(r'\d+(\.\d+)?', val)
        if digits:
            if kind == 'int':
                digits = int(digits.group())
            else:
                digits = float(digits.group())
        return digits
        
    
    def transform_one(self, row: dict[str, Any]):
        for field in self.QPT:
            if field == 'quantity':
                row[field] = self.to_numeric(row[field], 'int')  
            else: 
                row[field] = self.to_numeric(row[field], 'float')  
            
        for field in row:
            if field in self.QPT:
                pass
            elif field == 'timestamp':
                dt = parser.parse(row[field])
                row[field] = dt.isoformat()
            else:
                row[field] = row[field].strip().lower()
            
        row['total'] = row['price'] * row['quantity']
        return row
        
    def transform(self, validated_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        transformed_data: list[dict[str, Any]] = []
        for row in validated_data:
            transformed_data.append(self.transform_one(row))
        return transformed_data
            
        