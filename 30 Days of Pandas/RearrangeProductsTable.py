import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(products, columns=['product_id', 'store1', 'store2', 'store3'])
    df_melt = pd.melt(products, id_vars=['product_id'], value_vars=['store1', 'store2', 'store3'], 
    var_name='store', value_name='price')

    df = df_melt.dropna()

    return df