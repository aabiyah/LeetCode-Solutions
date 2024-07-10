import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    cooperation_counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')

    result = cooperation_counts[cooperation_counts['count'] >= 3]

    result = result[['actor_id', 'director_id']]

    return result