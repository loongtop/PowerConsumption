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
        }
    )

    # Define hover template
    hover_template = (
        '<b>Date:</b> %{customdata[0]}<br>'
        '<b>Humidity:</b> %{customdata[1]:.2f}RH<br>'
        '<b>Temperature:</b> %{customdata[2]:.2f}ºC<br>'
        '<b>WindSpeed:</b> %{customdata[3]:.2f}m/s<br>'
        '<b>Power Consumption:</b> %{customdata[4]:.2f}W<br>'
        '<b>Month:</b> %{customdata[5]}<br>'
        '<extra></extra>'  # This removes the secondary box with extra data
    )

    # Add hover template and custom data to the figure
    fig.update_traces(
        hovertemplate=hover_template,
        customdata=DailyData[
            ['date', 'Humidity', 'Temperature', 'WindSpeed', 'PowerConsumption_AllZones', 'MonthName']]
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
        yaxis=dict(fixedrange=True),   # Disable zoom on y-axis
    )

    return fig
