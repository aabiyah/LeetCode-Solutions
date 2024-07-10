import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge SalesPerson and Orders tables to find salespersons with orders to "RED"
    merged = pd.merge(sales_person, orders, on='sales_id', how='left')
    merged = pd.merge(merged, company[company['name'] == 'RED'], on='com_id', how='inner')

    # Extract sales_ids with orders to "RED"
    sales_ids_with_red_orders = merged['sales_id'].unique()

    # Filter salespersons who are not in the above list
    result = sales_person[~sales_person['sales_id'].isin(sales_ids_with_red_orders)]

    # Return only the 'name' column as required
    return result[['name']]