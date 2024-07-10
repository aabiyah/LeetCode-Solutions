import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employees, employee_uni, on='id', how='left')

    result = result[['unique_id', 'name']]

    result['unique_id'] = result['unique_id'].where(pd.notna(result['unique_id']), None)

    return result