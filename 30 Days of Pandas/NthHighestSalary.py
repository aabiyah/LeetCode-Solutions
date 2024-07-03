import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_df = employee.sort_values(by='salary', ascending=False)

    sorted_df = sorted_df.drop_duplicates(subset=['salary'], keep='first')

    if N <= 0 or N > len(sorted_df):
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [None]})

    nth_highest_salary = sorted_df.iloc[N-1]['salary']

    result_df = pd.DataFrame({'getNthHighestSalary({})'.format(N): [nth_highest_salary]})

    return result_df