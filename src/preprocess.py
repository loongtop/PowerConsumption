# -*- coding: utf-8 -*-

'''
    File name: preprocess.py
    Purpose: Contains functions to preprocess the data used in the visualization.
    Authors:
        - Yuashun Cui - 2404877
        - Samira Nazari - 2310647
        - Mohamad Hadi Ajami - 2227105
    Course: INF8808
    Python Version: 3.8

    This file provides the functionality to preprocess data for visualizing power consumption across different zones.
'''

import pandas as pd


# Function to preprocess raw data from a CSV file
def data_preprocess(file_path):
    """
    Preprocess the raw data from a CSV file for further analysis.

    Parameters:
        file_path (str): The file path to the CSV file.

    Returns:
        DataFrame: The preprocessed data as a pandas DataFrame.
    """
    if file_path is None:
        file_path = './assets/data/powerconsumption.csv'

    # Read the data from the CSV file
    df = pd.read_csv(file_path)
    
    # Convert the datetime column to datetime format
    df['datetime'] = pd.to_datetime(df['Datetime'])
    
    # Extract date and other time-based features
    df['date'] = df['datetime'].dt.date
    df['weekofyear'] = df['datetime'].dt.isocalendar().week
    df['day_of_week'] = df['datetime'].dt.dayofweek
    df['week'] = df['datetime'].dt.isocalendar().week
    df['hour'] = df['datetime'].dt.hour
    df['time'] = df['datetime'].dt.time
    df['DayName'] = df['datetime'].dt.day_name()
    df['MonthName'] = df['datetime'].dt.month_name()
    df['hourNo'] = df['datetime'].dt.hour + 1
    df['MonthNumber'] = df['datetime'].dt.month
    df['DayOfMonth'] = df['datetime'].dt.day
    df['DayOfYear'] = df['datetime'].dt.dayofyear
    
    # Calculate total power consumption across all zones
    df['PowerConsumption_AllZones'] = (df['PowerConsumption_Zone1'] + 
                                       df['PowerConsumption_Zone2'] + 
                                       df['PowerConsumption_Zone3'])
    df['Zone1'] = df['PowerConsumption_Zone1']
    df['Zone2'] = df['PowerConsumption_Zone2']
    df['Zone3'] = df['PowerConsumption_Zone3']

    return df

# Function to aggregate data on an hourly basis
def get_HourlyData(df):
    """
    Aggregate the data on an hourly basis.

    Parameters:
        df (DataFrame): The preprocessed data DataFrame.

    Returns:
        DataFrame: The hourly aggregated data.
    """
    # Columns to average and to find the maximum
    columns_to_avg = ['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows']
    columns_to_max = ['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3',
                      'PowerConsumption_AllZones']

    # Group by specified columns and aggregate
    HourlyData = df.groupby(
        ['date', 'week', 'hour', 'DayName', 'MonthName', 'hourNo', 'MonthNumber', 'DayOfMonth', 'DayOfYear',
         'weekofyear', 'day_of_week']
    ).agg(
        {**{col: 'mean' for col in columns_to_avg}, **{col: 'max' for col in columns_to_max}}
    ).reset_index()

    # Combine date and hour into a single datetime column for plotting
    HourlyData['datetime1'] = HourlyData['date'] + pd.to_timedelta(HourlyData['hour'], unit='h')

    return HourlyData

# Function to aggregate data on a daily basis
def get_DailyData(df):
    """
    Aggregate the data on a daily basis.

    Parameters:
        df (DataFrame): The preprocessed data DataFrame.

    Returns:
        DataFrame: The daily aggregated data.
    """
    # Columns to average and to find the maximum
    columns_to_avg = ['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows']
    columns_to_max = ['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3',
                      'PowerConsumption_AllZones']

    # Group by specified columns and aggregate
    DailyData = df.groupby(
        ['date', 'week', 'DayName', 'MonthName', 'MonthNumber', 'DayOfMonth', 'DayOfYear', 'day_of_week']
    ).agg(
        {**{col: 'mean' for col in columns_to_avg}, **{col: 'max' for col in columns_to_max}}
    ).reset_index()

    return DailyData
