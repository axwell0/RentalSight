import pandas as pd


def transform_customer():
    customer_path = 'source_data/customer.csv'
    customer_df = pd.read_csv(customer_path)
    address_path = "source_data/address.csv"
    address_df = pd.read_csv(address_path,dtype={'phone': str})



    #Removing unneeded columns
    df = customer_df.drop(['activebool', 'last_update','active','create_date',"store_id"], axis=1)
    customer_df = pd.merge(df, address_df[['address_id', 'phone']], on='address_id', how='left')
    customer_df["first_name"] = customer_df["first_name"].str.title()
    customer_df["last_name"] = customer_df["last_name"].str.title()
    customer_df["email"] = customer_df["email"].str.lower()



    customer_df.to_csv("customer.csv",index=False)
