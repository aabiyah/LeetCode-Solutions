import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    #Left join
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    no_orders = merged_df[merged_df['customerId'].isna()]
    return no_orders[['name']].rename(columns={'name': 'Customers'})

# Left DataFrame
# +----+-------+  
# | id | name  |
# +----+-------+
# |  1 | Joe   |
# |  2 | Henry |
# |  3 | Sam   |
# |  4 | Max   |
# +----+-------+

# Right DataFrame
# +----+------------+
# | id | customerId |
# +----+------------+
# |  1 | 3          |
# |  2 | 1          |
# +----+------------+

# DataFrame after Left Join
#  id_x   name   id_y  customerId
# 0     1    Joe   2.0         1.0
# 1     2  Henry   NaN         NaN
# 2     3    Sam   1.0         3.0
# 3     4    Max   NaN         NaN