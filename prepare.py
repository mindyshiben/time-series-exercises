import os
import requests
import pandas as pd
import acquire
from datetime import timedelta, datetime

def prep_store_data(df):
    df['sale_date'] = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %X %Z')
    df = df.set_index('sale_date').sort_index()
    df['day_of_week'] = df.index.day_name()
    df['month'] = df.index.month_name()
    df['sales_total'] = (df.sale_amount) * (df.item_price)
    return df

def prep_opsd_data(df):
    df['Date'] = pd.to_datetime(df.Date)
    df = df.set_index('Date').sort_index()
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    mean_w= df['Wind'].mean()
    df['Wind'].fillna(value=mean_w, inplace=True)
    mean_s= df['Solar'].mean()
    df['Solar'].fillna(value=mean_s, inplace=True)
    mean_ws= df['Wind+Solar'].mean()
    df['Wind+Solar'].fillna(value=mean_ws, inplace=True)
    
    return df