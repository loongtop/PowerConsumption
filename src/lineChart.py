# -*- coding: utf-8 -*-

'''
    File name: LineChart.py
    Purpose: Contains functions to create line charts for visualizing power consumption data.
    Author: 
    Course: INF8808
    Python Version: 3.8

    This file provides the functionality to generate line charts for daily power consumption data across different zones.
'''

import plotly.express as px
import hover_template as hover

# Function to create a line chart for power consumption over time
# def get_line_data(DailyData_df):
#     """
#     Generate a line chart for power consumption over time.
#
#     Parameters:
#         DailyData_df (DataFrame): The daily data DataFrame containing power consumption data.
#
#     Returns:
#         Figure: Plotly Figure object representing the line chart for power consumption over time.
#     """
#     # Transform the DataFrame to long-form for Plotly Express
#     DailyData_LineChart_df = DailyData_df.melt(
#         id_vars=['date'],
#         value_vars=['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3', 'PowerConsumption_AllZones'],
#         var_name='Zone',
#         value_name='PowerConsumption'
#     )
#
#     # Create the line chart
#     fig = px.line(
#         DailyData_LineChart_df,
#         x='date',
#         y='PowerConsumption',
#         color='Zone',
#         title='Power Consumption Over Time',
#         labels={
#             'date': 'Date',
#             'PowerConsumption': 'Power Consumption (kW)'
#         },
#         line_group='Zone',
#         hover_name='Zone',
#         hover_data={'PowerConsumption': False}  # Exclude PowerConsumption from hover info
#     )
#
#     # Update legend labels to be more readable
#     fig.for_each_trace(lambda trace: trace.update(
#         name=trace.name.replace('PowerConsumption_', ' ')
#     ))
#
#     # Update hover template
#     fig.update(data=[{'hovertemplate': hover.get_line_chart_hover_template()}])
#
#     # Set layout options to prevent zooming
#     fig.update_layout(
#         yaxis=dict(fixedrange=True)   # Disables zoom on y-axis
#     )
#
#     return fig


import plotly.express as px


def get_line_data(DailyData_df):
    """
    Generate a line chart for power consumption over time.

    Parameters:
        DailyData_df (DataFrame): The daily data DataFrame containing power consumption data.

    Returns:
        Figure: Plotly Figure object representing the line chart for power consumption over time.
    """
    # Transform the DataFrame to long-form for Plotly Express
    DailyData_LineChart_df = DailyData_df.melt(
        id_vars=['date'],
        value_vars=['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3',
                    'PowerConsumption_AllZones'],
        var_name='Zone',
        value_name='PowerConsumption'
    )

    # Create the line chart with different line styles based on 'Zone'
    fig = px.line(
        DailyData_LineChart_df,
        x='date',
        y='PowerConsumption',
        color='Zone',
        title='Power Consumption Over Time',
        labels={
            'date': 'Date',
            'PowerConsumption': 'Power Consumption (kW)'
        },
        line_group='Zone',
        hover_name='Zone',
        hover_data={'PowerConsumption': False},  # Exclude PowerConsumption from hover info
        line_dash='Zone'  # Use 'Zone' to differentiate line styles based on categorical variable
    )

    # Update legend labels to be more readable
    fig.for_each_trace(lambda trace: trace.update(
        name=trace.name.replace('PowerConsumption_', ' ')
    ))

    # Update hover template
    fig.update(data=[{'hovertemplate': hover.get_line_chart_hover_template()}])

    # Set layout options to prevent zooming
    fig.update_layout(
        yaxis=dict(fixedrange=True)  # Disables zoom on y-axis
    )

    return fig

