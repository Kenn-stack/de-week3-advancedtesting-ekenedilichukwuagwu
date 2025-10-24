from typing import Any

class Analyzer:
    def total_revenue(self, transformed_data: list[dict[str, Any]]) -> float:
        revenue_list: list[float] = [revenue['total'] for revenue in transformed_data]
        total_rev: float = round(sum(revenue_list), 2)
        return total_rev
        
        
    def average_revenue(self, transformed_data: list[dict[str, Any]]) -> float:
        revenue_list: list[float] = [revenue['total'] for revenue in transformed_data]
        avg_rev: float = round(sum(revenue_list) / len(revenue_list), 2)
        return avg_rev
        
        
    def churn_analysis(self, transformed_data: list[dict[str, Any]]) -> dict[str, int]:
        total_paid: int = len([data['payment_status'] for data in transformed_data if data['payment_status'] == 'paid'])
        total_pending: int = len([data['payment_status'] for data in transformed_data if data['payment_status'] == 'pending'])
        total_refunded: int = len([data['payment_status'] for data in transformed_data if data['payment_status'] == 'refunded'])
        return {'total_paid': total_paid, 'total_pending': total_pending, 'total_refunded': total_refunded}
        
        