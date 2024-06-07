import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame: 

    # Line 3 defines a function named createDataframe that takes a parameter called student_data and returns a pd.DataFrame, for which the columns are defined below.

    df = pd.DataFrame(student_data, columns=['student_id','age'])
    return df