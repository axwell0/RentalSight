import pandas as pd

def create_inventory_snapshot():

    store_df = pd.read_csv('store.csv')
    film_df = pd.read_csv('film.csv')
    rental_df = pd.read_csv('rental.csv')

    inventory_df = pd.read_json('source_data/inventory.json').drop(["last_update"],axis=1)

    rental_quantity = rental_df.groupby(["inventory_id"]).size().reset_index(name="rental_quantity")



    merged_df = inventory_df.merge(rental_quantity, on='inventory_id', how='outer')
    merged_df['rental_quantity'] = merged_df['rental_quantity'].fillna(0).astype(int)

    inventory = merged_df.groupby(['film_id', 'store_id'])['rental_quantity'].sum().reset_index(name='rental_quantity')



    film_store_count = inventory_df.groupby(['store_id', 'film_id']).size().reset_index(name='stock_quantity')["stock_quantity"]

    inventory["stock_quantity"] = film_store_count

    inventory.to_csv('inventory_snapshot.csv',index=False,header=True)