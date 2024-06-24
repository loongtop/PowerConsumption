# -*- coding: utf-8 -*-

'''
    File name: BubblePlot.py
    Purpose: Contains functions to create bubble plots for visualizing power consumption data.
    Author: 
    Course: INF8808
    Python Version: 3.8

    This file provides the functionality to generate bubble plots for daily power consumption data.
'''

from plotly import express as px

def get_bubble_plot(DailyData, x_col, y_col):
    """
    Generate a bubble plot for power consumption with dynamic x and y axes.

    Parameters:
        DailyData (DataFrame): The daily data DataFrame.
        x_col (str): The column name for the x-axis.
        y_col (str): The column name for the y-axis.

    Returns:
        Figure: Plotly Figure object representing the bubble plot.
    """
    fig = px.scatter(
        DailyData,
        x=x_col,
        y=y_col,
        size='PowerConsumption_AllZones',  # Size bubbles by PowerConsumption_AllZones
        color='PowerConsumption_AllZones',  # Color bubbles by PowerConsumption_AllZones
        title=f'Bubble Plot: {x_col} vs. {y_col} with Power Consumption Size',
        labels={
            x_col: x_col.replace('_', ' '),  # Replace underscores with spaces for readability
            y_col: y_col.replace('_', ' '),
            'PowerConsumption_AllZones': 'Power Consumption'
        },
        hover_data=['DayName', 'MonthName']  # Include additional data in hover info
    )

    # Customize bubble plot appearance
    fig.update_traces(
        marker=dict(
            line=dict(width=1, color='DarkSlateGrey')  # Set marker line properties
        ),
        selector=dict(mode='markers')  # Set marker mode to 'markers'
    )

    # Customize layout
    fig.update_layout(
        xaxis_title=x_col.replace('_', ' '),  # Set x-axis title dynamically
        yaxis_title=y_col.replace('_', ' '),  # Set y-axis title dynamically
        title=f'Bubble Plot: {x_col} vs. {y_col} with Power Consumption Size',
        dragmode='pan',  # Enable panning mode
        xaxis=dict(fixedrange=True),  # Disable zoom on x-axis
        yaxis=dict(fixedrange=True)   # Disable zoom on y-axis
    )

    return fig


def get_bubble_plot_colour(DailyData, x_col, y_col):
    """
    Generate a bubble plot for power consumption with specific colors.

    Parameters:
        DailyData (DataFrame): The daily data DataFrame.
        x_col (str): The column name for the x-axis.
        y_col (str): The column name for the y-axis.

    Returns:
        Figure: Plotly Figure object representing the bubble plot with color.
    """
    fig = px.scatter(
        DailyData,
        x=x_col,
        y=y_col,
        size='PowerConsumption_AllZones',  # Size bubbles by PowerConsumption_AllZones
        color='PowerConsumption_AllZones',  # Color bubbles by PowerConsumption_AllZones
        title=f'Bubble Plot: {x_col} vs. {y_col} with Power Consumption Size and Color',
        labels={
            x_col: x_col.replace('_', ' '),  # Replace underscores with spaces for readability
            y_col: y_col.replace('_', ' '),
            'PowerConsumption_AllZones': 'Power Consumption'
        },
        color_continuous_scale='Viridis',  # Use Viridis color scale
        size_max=20,  # Maximum bubble size
        hover_data=['date']  # Include additional hover data
    )

    # Customize layout
    fig.update_layout(
        dragmode='pan',  # Enable panning mode
        xaxis=dict(fixedrange=True),  # Disable zoom on x-axis
        yaxis=dict(fixedrange=True)   # Disable zoom on y-axis
    )

    return fig
