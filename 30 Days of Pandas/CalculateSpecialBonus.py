import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employees, columns=['employee_id', 'name', 'salary'])
    df['bonus'] = 0
    condition = (~df['name'].str.startswith('M')) & (df['employee_id'] % 2 != 0)
    df.loc[condition, 'bonus'] = df['salary'] #assigns the values from the salary column to the bonus column for all rows where the condition is True.
    df = df.sort_values(by='employee_id', ascending=True)
    return df[['employee_id', 'bonus']]