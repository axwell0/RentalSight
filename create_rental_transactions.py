import pandas as pd


def create_rental_transactions():
    payment_path="source_data/transaction.csv"
    rental_df = pd.read_csv("rental.csv",dtype={"inventory_id":str})
    film_df = pd.read_csv("film.csv",dtype={"film_id":str,"allowed_rental_duration":int})

    inventory_df = pd.read_json('source_data/inventory.json',dtype={"inventory_id":str,"film_id":str,"store_id":str})
    payment_df = pd.read_csv(payment_path)
    payment_df = payment_df.drop(["payment_date","staff_id"],axis=1)

    payment_df = payment_df.merge(rental_df[["return_date","rental_date","rental_id","inventory_id"]],on="rental_id",how="left")
    payment_df=payment_df.merge(inventory_df[["film_id","store_id","inventory_id"]],on="inventory_id",how="left")

    payment_df = payment_df.merge(film_df[['film_id',"allowed_rental_duration"]],on="film_id",how="left")
    payment_df['return_date'] = pd.to_datetime(payment_df['return_date'])
    payment_df['rental_date'] = pd.to_datetime(payment_df['rental_date'])


    payment_df["rental_duration"] = (payment_df['return_date'] - payment_df['rental_date']).dt.days

    payment_df['late_fees'] = (payment_df['rental_duration'] - payment_df['allowed_rental_duration']).clip(lower=0)
    late_fee_rate = 1
    payment_df['late_fees'] = payment_df['late_fees'] * late_fee_rate

    columns_to_extract = ["customer_id", "film_id", "store_id", "rental_id", "amount", "rental_duration", "late_fees"]
    rental_transactions_df = payment_df[columns_to_extract]
    rental_transactions_df = rental_transactions_df.rename(columns={"amount": "rental_price"}).sort_values(by=['customer_id', 'film_id', 'store_id'])


    rental_transactions_df.to_csv('rental_transactions.csv',index=False,header=True)