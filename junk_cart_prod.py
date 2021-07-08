#Creates a cartesian product of all junk flags to create a junk dimension for a data warehouse star schema
#To be used in Tableau Prep
#No output function needed since output df uses the same fields as the input df

import pandas as pd
import itertools

def create_dim_junk(df):

    df = df.drop(['Junk_Key'], axis=1)
    headers = tuple(df.columns)

    #Gets each column's unique values
    unique_val_per_col = tuple([tuple(df[col].unique()) for col in headers])
    cart_product = set()

    for element in itertools.product(*unique_val_per_col):
        cart_product.add(element)

    df = pd.DataFrame(cart_product, columns=headers)
    df.index = df.index + 1
    df['Junk_Key'] = df.apply(lambda x: str(x.name), axis=1)

    return df

