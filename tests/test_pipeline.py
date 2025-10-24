import pytest
from order_pipeline.reader import Reader
from order_pipeline.validator import Validator
from order_pipeline.transformer import Transformer
from order_pipeline.analyzer import Analyzer
from order_pipeline.exporter import Exporter



def test_reader():
    good_reader = Reader().read('shoplink.json')
    assert good_reader[:1] == [{'order_id': 'ORD001', 'timestamp': '2025-10-19T08:00:00Z', 'item': 'Wireless Mouse', 'quantity': 2, 'price': '$15.99', 'total': '$31.98', 'payment_status': 'paid'}]
    
    with pytest.raises(ValueError):
        Reader().read('tests/shoplink.csv')
        
    with pytest.raises(ValueError):
        Reader().read('tests/bad_shoplink.json')    
        

def test_validator():
    reader = Reader().read('tests/missing_field.json')
    validated_data = Validator().validate(reader)
    assert len(validated_data) == 1
    
    
def test_transformer():
    reader = Reader().read('shoplink.json')
    validated_data = Validator().validate(reader)
    transformed_data = Transformer().transform(validated_data)[0]
    
    assert isinstance(transformed_data['quantity'], int)
    assert isinstance(transformed_data['total'], float)
    assert isinstance(transformed_data['price'], float)
    assert transformed_data['item'].islower()
    assert transformed_data['order_id'].islower()


def test_analyzer():
    reader = Reader().read('shoplink.json')
    validated_data = Validator().validate(reader)
    transformed_data = Transformer().transform(validated_data)
    total_rev = Analyzer().total_revenue(transformed_data)
    average_rev = Analyzer().average_revenue(transformed_data)
    churn_analysis = Analyzer().churn_analysis(transformed_data)

    assert total_rev == 15091.48
    assert average_rev == 2515.25
    assert churn_analysis == {'total_paid': 4, 'total_pending': 1, 'total_refunded': 1}
    
    
def test_exporter():
    reader = Reader().read('shoplink.json')
    validated_data = Validator().validate(reader)
    transformed_data = Transformer().transform(validated_data)
    export = Exporter().export_to_json_file(transformed_data)
    
    assert export == 'Done'
    
    
    
    
    
    

    