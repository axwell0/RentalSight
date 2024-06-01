import pandas as pd

def transform_address():

    address_path = "source_data/address.csv"
    address_df = pd.read_csv(address_path, dtype={"postal_code":str})
    city_path = "source_data/city.csv"
    city_df = pd.read_csv(city_path)
    country_path = "source_data/country.csv"
    country_df = pd.read_csv(country_path)
    city_df = pd.merge(city_df,country_df[["country","country_id"]],on="country_id",how="left")
    address_df = address_df.drop(["last_update","phone","address2"],axis=1)
    address_df = pd.merge(address_df,city_df[["city_id","city","country"]],on="city_id",how="left").drop(["city_id"],axis=1)

    address_df.loc[address_df['district'] == 'Alberta', 'postal_code'] = '30303'
    address_df.loc[address_df['district'] == 'QLD', 'postal_code'] = '20220'

    address_df.to_csv("address.csv",index=False)