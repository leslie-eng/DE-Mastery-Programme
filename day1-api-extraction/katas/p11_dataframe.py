COLUMNS = ['customer_id', 'name', 'email', 'address_city', 'address_city_geo_lat']


from p09_flatten import flatten
from p10_core_fields import extract_core_fields
import pandas as pd

def to_dataframe(rows):
    flatten_dict = extract_core_fields(flatten(rows))
    
    df = pd.DataFrame(flatten_dict)
    
    df.reindex(columns=COLUMNS)
    
    assert len(COLUMNS) == 15 and len(set(COLUMNS)) == 15
    
    return df
    