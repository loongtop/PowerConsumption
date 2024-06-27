# -*- coding: utf-8 -*-

'''
    File name: globals.py
    Purpose: Load and preprocess power consumption data.
    Authors:
        - Yuashun Cui - 2404877
        - Samira Nazari - 2310647
        - Mohamad Hadi Ajami - 2227105
    Course: INF8808
    Python Version: 3.8

    This file provides functionality to load and preprocess data for visualizing power consumption.
'''

import preprocess

# Define the file path for the data
file_path = './assets/data/powerconsumption.csv'

# Load and preprocess the data
df = preprocess.data_preprocess(file_path)

# Generate hourly and daily data DataFrames
df_hourly = preprocess.get_HourlyData(df)
df_daily = preprocess.get_DailyData(df)
