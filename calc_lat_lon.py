#Converts cartographic projections into latitude and longitude
#To be used in Tableau Prep

from pyproj import Transformer
import pandas as pd

transformer = Transformer.from_crs('epsg:3857', 'epsg:4326')

def add_lat_lon(df):

    df['LAT'], df['LON'] = transformer.transform(df['X'], df['Y'])
    df.drop(['X','Y'], axis=1, inplace=True)

    return df

#Tableau Prep function, specifies the attributes and their types in the output table
def get_output_schema():
    return pd.DataFrame({
        'Folio' : prep_string(),
        'Property Address' : prep_string(),
        'zip' : prep_string(),
        'Municipality ID' : prep_string(),
        'Municipality' : prep_string(),
        'LAT' : prep_decimal(),
        'LON' : prep_decimal()
    })