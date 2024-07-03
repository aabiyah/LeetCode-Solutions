import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    sorted_df = employee.sort_values(by='salary', ascending=False)

    sorted_df = sorted_df.drop_duplicates(subset=['salary'], keep='first')

    if len(sorted_df) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    second_highest_salary = sorted_df.iloc[1]['salary']

    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})

    return result_df