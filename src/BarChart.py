'''
    File name: BarChart.py
    Purpose: Contains functions to create bar charts for visualizing power consumption data.
    Author: 
    Course: INF8808
    Python Version: 3.8

    This file provides the functionality to generate bar charts for hourly power consumption data.
'''

from datetime import datetime
import plotly.express as px
import hover_template as hover

def to_date_format(HourlyData, date_str):
    """
    Filter the hourly data for a specific date.

    Parameters:
        HourlyData (DataFrame): The hourly data DataFrame.
        date_str (str): Date string in the format 'YYYY-MM-DD'.

    Returns:
        DataFrame: DataFrame containing data for the specified date.
    """
    # Convert string to date format
    date_format = datetime.strptime(date_str, '%Y-%m-%d').date()
    specific_day_data = HourlyData[HourlyData['date'] == date_format]

    return specific_day_data

def get_bar_chart(HourlyData, date_str):
    """
    Generate a bar chart for power consumption data on a specific date.

    Parameters:
        HourlyData (DataFrame): The hourly data DataFrame.
        date_str (str): Date string in the format 'YYYY-MM-DD'.

    Returns:
        Figure: Plotly Figure object representing the bar chart.
    """
    # Filter the data for the specified date
    specific_day_data = to_date_format(HourlyData, date_str)
    
    # Create a bar chart using Plotly Express
    fig = px.bar(
        specific_day_data,
        x='hourNo',
        y='PowerConsumption_AllZones',
        labels={
            'hourNo': 'Hour',
            'PowerConsumption_AllZones': 'Power Consumption (KW)'
        },
        title=f'Power Consumption for {date_str}'
    )
    
    # Update hover template
    fig.update(
        data=[{
            'hovertemplate': hover.get_barchart_hover_template()
        }]
    )
    
    # Set layout options
    fig.update_layout(dragmode='pan')
    fig.update_layout(
        xaxis=dict(fixedrange=True),  # Disables zoom on x-axis
        yaxis=dict(fixedrange=True)   # Disables zoom on y-axis
    )

    return fig