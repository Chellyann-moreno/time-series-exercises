# IMPORTS 

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns



#FUNCTIONS


def store_data():
    """
    Reads the 'ts_superstore.csv' file and performs data preprocessing on it.

    Returns:
        df (DataFrame): Processed data frame containing sales data for a superstore.
    
    """
    df = pd.read_csv('ts_superstore.csv', index_col=0)
    df.columns = df.columns.str.lower()
    df.sale_date = df.sale_date.str.replace('00:00:00 GMT', '')
    df.sale_date = df.sale_date.str.strip()
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y')
    df = df.set_index('sale_date').sort_index()
    df['month'] = df.index.month
    df['month_name'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df.item_price + df.sale_amount
    return df

def plot_distributions(dataframe):
    """
    Generate distribution plots for each column in the given data frame.

    Args:
        dataframe (DataFrame): Input data frame containing numerical columns.

    Returns:
        None
    
    """
    for column in dataframe.columns:
        sns.histplot(data=dataframe, x=column, kde=True)
        plt.title(f"Distribution of {column}")
        plt.show()

def plot_one_distribution(dataframe, column):
    """
    Generate a distribution plot for a specific column of a data frame.

    Args:
        dataframe (DataFrame): Input data frame.
        column (str): Name of the column to plot.

    Returns:
        None
    
    """
    sns.histplot(data=dataframe, x=column, kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()

def opsd_data():
    """
    Reads the 'opsd_germany_daily.csv' file and performs data preprocessing on it.

    Returns:
        df (DataFrame): Processed data frame containing daily electricity consumption and production data for Germany.
    
    """
    df = pd.read_csv('opsd_germany_daily.csv')
    df.columns = df.columns.str.lower()
    df.date = df.date.astype('datetime64')
    df = df.set_index('date')
    df = df.sort_index()
    df['month'] = df.index.month
    df['month_name'] = df.index.month_name()
    df['year'] = df.index.year
    df = df.bfill()
    return df