from .reader import Reader
from .validator import Validator
from .transformer import Transformer
from .analyzer import Analyzer
from .exporter import Exporter


class ShopLinkETL:
    def __init__(self) -> None:
        self.reader = Reader()
        self.validator = Validator()
        self.transformer = Transformer()
        self.analyzer = Analyzer()
        self.exporter = Exporter()
        
        
    def run(self):
        print('Starting ShopLinkEtL run')
        raw = self.reader.read('shoplink.json')
        print(f'Read {len(raw)} raw rows')
        valid = self.validator.validate(raw)
        print(f'Validated {len(valid)} rows')
        transform = self.transformer.transform(valid)
        print(f'Transformed to {len(transform)} rows')
        print(f'Total Revenue: {self.analyzer.total_revenue(transform)}')
        print(f'Average Revenue: {self.analyzer.average_revenue(transform)}')
        print(f'Churn Analysis: {self.analyzer.churn_analysis(transform)}')
        self.exporter.export_to_json_file(transform)
        print(f'Exported {len(transform)} rows to shoplink_cleaned.json')

        
        
ShopLinkETL().run()    

