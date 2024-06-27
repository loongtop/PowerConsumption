# -*- coding: utf-8 -*-

'''
    File name: ScatterPlotChart.py
    Purpose: Contains functions to create scatter plot charts for visualizing power consumption data.
    Authors:
        - Yuashun Cui - 2404877
        - Samira Nazari - 2310647
        - Mohamad Hadi Ajami - 2227105
    Course: INF8808
    Python Version: 3.8

    This file provides the functionality to generate scatter plot charts for daily power consumption data.
'''

import plotly.express as px
import hover_template as hover
from globals import df


# Function to create a scatter plot chart based on user-specified columns
def get_ScatterPlotChart(DailyData, x_col, y_col):
    """
    Generate a scatter plot chart for two specified columns.

    Parameters:
        DailyData (DataFrame): The daily data DataFrame.
        x_col (str): The column name for the x-axis.
        y_col (str): The column name for the y-axis.

    Returns:
        Figure: Plotly Figure object representing the scatter plot chart.
    """
    # Define the title of the chart
    title = f'{x_col} vs. {y_col}'

    # Create the scatter plot
    fig = px.scatter(
        DailyData,
        x=x_col,
        y=y_col,
        title=title
    )

    # Disable zoom on axes
    fig.update_layout(
        dragmode='pan',
        xaxis=dict(fixedrange=True),
        yaxis=dict(fixedrange=True)
    )

    # Update hover template
    fig.update(
        data=[{
            'hovertemplate': hover.get_scatterplotchart_hover_template(x_col, y_col)
        }]
    )

    return fig


def get_ScatterPlotChart_3Zones(x_col='Temperature'):
    """
    Generate a scatter plot chart showing the correlation between a selected column 
    (e.g., Temperature, WindSpeed, Humidity) and power consumption across three zones.

    Parameters:
        x_col (str): The column name for the x-axis. Defaults to 'Temperature'.

    Returns:
        Figure: Plotly Figure object representing the scatter plot chart for three zones.
    """
    
    # Define columns for averaging and finding the maximum
    columns_to_avg = ['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows']
    columns_to_max = ['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3', 'PowerConsumption_AllZones']

    # Group by specified columns and aggregate
    DailyData_df = df.groupby(
        ['date', 'week', 'DayName', 'MonthName', 'MonthNumber', 'DayOfMonth', 'DayOfYear', 'day_of_week']
    ).agg(
        {**{col: 'mean' for col in columns_to_avg}, **{col: 'max' for col in columns_to_max}}
    ).reset_index()

    # Create initial scatter plot for Zone 1
    fig = px.scatter(
        DailyData_df,
        x=x_col,
        y='PowerConsumption_Zone1',
        title=f'Correlation between {x_col} and Power Consumption',
        labels={x_col: x_col, 'PowerConsumption_Zone1': 'Power Consumption'},
        opacity=0.7,
    )

    # Update trace for Zone 1 with customdata and legend
    fig.update_traces(
        name='Zone 1',
        customdata=DailyData_df['date'],  # Add date as customdata
        showlegend=True,
        marker=dict(size=8),
    )

    # Add trace for PowerConsumption_Zone2
    fig.add_scatter(
        x=DailyData_df[x_col],
        y=DailyData_df['PowerConsumption_Zone2'],
        mode='markers',
        name='Zone 2',
        customdata=DailyData_df['date'],
        marker=dict(size=8),
        showlegend=True,
    )

    # Add trace for PowerConsumption_Zone3
    fig.add_scatter(
        x=DailyData_df[x_col],
        y=DailyData_df['PowerConsumption_Zone3'],
        mode='markers',
        name='Zone 3',
        customdata=DailyData_df['date'],
        marker=dict(size=8),
        showlegend=True,
    )

    # Update layout for legend and axis titles
    fig.update_layout(
        legend=dict(
            title='Zone',
            orientation='v',  # Vertical legend
            yanchor='middle', y=0.5,  # Center vertically
            xanchor='left', x=1.05,  # Place legend to the right of the plot
            bgcolor='rgba(255, 255, 255, 0.5)',  # Semi-transparent background
            bordercolor='white',  # Border color
            borderwidth=1,  # Border width
            font=dict(
                size=12,  # Font size
                color='black'  # Font color
            )
        ),
        margin=dict(r=200),  # Add right margin to make space for the legend
        xaxis=dict(title=x_col, fixedrange=True),  # Update x-axis title dynamically
        yaxis=dict(title='Power Consumption(w)', fixedrange=True),  # Update y-axis title and disable zoom
        dragmode='pan',
    )

    fig.update_traces(marker=dict(symbol='square'))
    # Add hover template at the end
    hover_template = hover.get_scatterplotchartforenergy_hover_template(x_col)
    fig.update_traces(hovertemplate=hover_template)

    return fig
