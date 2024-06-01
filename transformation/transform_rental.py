import pandas as pd

def transform_rental():
    rental_path=("source_data/rental.csv")
    rental_df = pd.read_csv(rental_path)
    df= rental_df.drop(["staff_id","last_update"],axis=1)
    df["rental_date"] = pd.to_datetime(df["rental_date"], format='%Y-%m-%d %H:%M:%S%z')
    df['day'] = df['rental_date'].dt.day
    df['month'] = df['rental_date'].dt.month
    df['year'] = df['rental_date'].dt.year
    df["rental_id"] = df["rental_id"] -1
    day_df = df[['day']].drop_duplicates().reset_index(drop=True)
    month_df = df[['month']].drop_duplicates().reset_index(drop=True)
    year_df = df[['year']].drop_duplicates().reset_index(drop=True)
    day_df['day_id'] = day_df.index + 1
    month_df['month_id'] = month_df.index + 1
    year_df['year_id'] = year_df.index + 1
    df = pd.merge(df, day_df, on='day', how='left')
    df = pd.merge(df, month_df, on='month', how='left')
    df = pd.merge(df, year_df, on='year', how='left')
    df = df.drop(["day","month","year"],axis=1)

    import calendar
    month_df['month_name'] = month_df['month'].apply(lambda x: calendar.month_name[x])

    df.to_csv("rental.csv",index=False)
    day_df.to_csv('day.csv',index=False)
    month_df.to_csv('month.csv',index=False)
    year_df.to_csv('year.csv',index=False)