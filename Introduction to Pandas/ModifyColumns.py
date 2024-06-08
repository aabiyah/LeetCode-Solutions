import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employees, columns = ['name', 'salary'])
    df['salary'] = df['salary']*2
    return df