import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students, columns = ['student_id', 'name', 'age'])
    df_no_missing = df.dropna()
    return df_no_missing