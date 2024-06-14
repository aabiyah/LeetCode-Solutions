import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(users, columns=['user_id', 'name'])
    df['name'] = df['name'].apply(lambda x: x.capitalize())
    users = df.sort_values(by='user_id', ascending=True)
    return users