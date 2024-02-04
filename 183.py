import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    customers=customers[~customers["id"].isin(orders["customerId"])]

    result=customers[["name"]].rename(columns={"name":"Customers"})

    return result
    
