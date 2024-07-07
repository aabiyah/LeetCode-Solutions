import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    joined_table = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner')

    joined_table['max_salary'] = joined_table.groupby('departmentId')['salary'].transform('max')

    result = joined_table[joined_table['salary'] == joined_table['max_salary']]

    result = result[['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']

    return result