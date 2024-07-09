import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_counts = orders.groupby('customer_number').size().reset_index(name='order_count')

    max_orders = order_counts[order_counts['order_count'] == order_counts['order_count'].max()]

    result = max_orders[['customer_number']]

    return resultCu