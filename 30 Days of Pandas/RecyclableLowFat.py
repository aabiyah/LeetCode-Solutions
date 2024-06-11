import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df[['product_id']] 

    #The double brackets [['product_id']] ensure that the result is a DataFrame, not a Series.