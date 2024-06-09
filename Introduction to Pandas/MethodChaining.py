import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(animals, columns = ['name', 'species', 'age', 'weight'])
    df_filtered = df[df['weight'] > 100]
    df_sorted = df_filtered.sort_values(by='weight', ascending=False)

    result_df = df_sorted[['name']]

    return result_df