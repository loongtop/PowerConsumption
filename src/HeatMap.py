'''
    File name: HeatMap.py
    Purpose: Contains functions to create heatmaps for visualizing power consumption data.
    Author: 
    Course: INF8808
    Python Version: 3.8

    This file provides the functionality to generate heatmaps for daily power consumption data across different zones.
'''

import plotly.graph_objects as go
import hover_template as hover


def get_heatmap(DailyData, zone_col, title_suffix):
    """
    Generate a heatmap for power consumption for a specified zone.

    Parameters:
        DailyData (DataFrame): The daily data DataFrame.
        zone_col (str): The column name for the zone's power consumption data.
        title_suffix (str): The suffix to append to the title for the heatmap.

    Returns:
        Figure: Plotly Figure object representing the heatmap for the specified zone.
    """
    # Filter data for the specified zone
    zone_data = DailyData[['week', 'DayName', 'DayOfYear', 'MonthName', zone_col]]

    # Ensure unique combinations of 'DayOfYear' and 'week'
    zone_data_unique = zone_data.drop_duplicates(subset=['week', 'DayOfYear'])
    zone_data_unique['MonthYear'] = zone_data_unique['MonthName'] + ' ' + (
        zone_data_unique['DayOfYear'] // 1000).astype(str)
    unique_months = zone_data_unique.groupby('MonthYear')['week'].min().reset_index()

    # Create the heatmap
    fig = go.Figure(data=go.Heatmap(
        z=zone_data_unique[zone_col],
        x=zone_data_unique['week'],
        y=zone_data_unique['DayName'],
        customdata=zone_data_unique['MonthYear'],
        colorscale='Viridis',
        colorbar=dict(title='Power Consumption'),
    ))

    # Update the layout
    fig.update_layout(
        title=f'Power Consumption {title_suffix}',
        yaxis_title="Day of Week",
        xaxis=dict(
            tickvals=unique_months['week'],
            ticktext=unique_months['MonthYear'].str.split().str[0],
            fixedrange=True  # Disables zoom on x-axis
        ),
        yaxis=dict(fixedrange=True)  # Disables zoom on y-axis
    )

    fig.update(data=[{'hovertemplate': hover.get_heatmap_hover_template()}])
    return fig
