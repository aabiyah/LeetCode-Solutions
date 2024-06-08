import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(customers, columns = ['customer_id', 'name', 'email'])
    df_no_duplicates = df.drop_duplicates(subset=['email'], keep='first')
    return df_no_duplicates