#Tableau Prep Output was not working
#This exports to csv the dataframe passed to it from Tableau Prep

import pandas as pd

path = r'Output.csv'

def output_to_csv(df):

    df.to_csv(path, index=False)

    return df