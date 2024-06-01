import pandas as pd


def transform_store():
    store_path = "source_data/store.csv"
    store_df = pd.read_csv(store_path)

    store_df = store_df.drop(["last_update","manager_staff_id"],axis = 1)
    store_df["name"] = ["Cinematic Delights Rentals","Blockbuster video store"]
    store_df.to_csv("store.csv",index=False)

