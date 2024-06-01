import pandas as pd

def transform_film():
    film_path = 'source_data/film.json'
    film_df = pd.read_json(film_path)
    film_category_path=("source_data/film_category.json")
    category_path="source_data/category.json"
    category_df = pd.read_json(category_path)
    language_path="source_data/language.json"
    lang_df = pd.read_json(language_path)
    film_category_df = pd.read_json(film_category_path)
    # Display the DataFrame
    film_df = film_df.drop(["special_features","fulltext","last_update","replacement_cost","original_language_id"],axis=1)

    film_df = pd.merge(film_df,lang_df[["language_id","name"]],on="language_id",how="left").drop(["language_id"],axis=1)
    film_category_df = pd.merge(film_category_df,category_df[["category_id","name"]],on="category_id",how="left").drop(["last_update"],axis=1)

    film_df = pd.merge(film_df,film_category_df[["film_id","name"]],on="film_id",how="left")
    film_df = film_df.rename(columns={"name_x":"language","name_y":"genre","rental_duration":"allowed_rental_duration"})
    film_df = film_df.drop(["rental_rate"], axis=1)
    film_df.to_csv("film.csv",index=False)
