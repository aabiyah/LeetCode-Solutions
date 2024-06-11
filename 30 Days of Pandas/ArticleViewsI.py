import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[(views['author_id'] == views['viewer_id'])]
    df = df.rename(columns={'author_id': 'id'})
    df = df.drop_duplicates()
    df = df.sort_values(by='id', ascending=True)
    return df[['id']]