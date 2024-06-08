import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students, columns=['student_id', 'name', 'age'])
    selected_columns = df.loc[df['student_id'] == 101,['name', 'age']] 

#selects rows from the DataFrame df where the 'student_id' is 101, and from those selected rows, it extracts the 'name' and 'age' columns

    return selected_columns