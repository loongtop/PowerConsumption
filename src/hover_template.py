# -*- coding: utf-8 -*-

'''
    File name: hover_template.py
    Purpose: Contains functions to set hover templates for various chart types in the power consumption data visualization project.
    Authors:
        - Yuashun Cui - 2404877
        - Samira Nazari - 2310647
        - Mohamad Hadi Ajami - 2227105
    Course: INF8808
    Python Version: 3.8

    This file provides the functionality to generate hover templates for line charts, heatmaps, bar charts, and scatter plots.
'''

# Dictionary for data units
data_dict = {
    'Humidity': '%',
    'Temperature': 'ºC',
    'WindSpeed': 'm/s'
}

def get_line_chart_hover_template():
    '''
        Sets the template for the hover tooltips in line charts.
        
        Returns:
            str: The content of the tooltip.
    '''
    hover_template = (
        "<b>Date</b>: %{x}<br>"
        "<b>Zone</b>: %{customdata[0]}<br>"
        "<b>Power Consumption</b>: %{y:.2f} W<br>"
        "<extra></extra>"
    )
    return hover_template

def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in heatmaps.

        Returns:
            str: The content of the tooltip.
    '''
    hover_template = (
        "<span style='font-weight:bold'>Date</span>: %{customdata[0]}<br>"
        "<span style='font-weight:bold'>Week of the Year</span>: %{x}<br>"
        "<span style='font-weight:bold'>Day of the Week</span>: %{y}<br>"
        "<span style='font-weight:bold'>Power Consumption</span>: %{z} W<br>"
        "<extra></extra>"
    )
    return hover_template

def get_barchart_hover_template():
    '''
        Sets the template for the hover tooltips in bar charts.

        Returns:
            str: The content of the tooltip.
    '''
    hover_template = (
        "<span style='font-weight:bold'>Hour</span>: %{x}<br>"
        "<span style='font-weight:bold'>Power Consumption</span>: %{y:.2f} W<br>"
        "<extra></extra>"
    )
    return hover_template

def get_scatterplotchart_hover_template(x_col, y_col):
    '''
        Sets the template for the hover tooltips in scatter plots.
        
        Parameters:
            x_col (str): The name of the x-axis column.
            y_col (str): The name of the y-axis column.

        Returns:
            str: The content of the tooltip.
    '''
    def get_unit(col):
        return data_dict.get(col, '')

    x_unit = get_unit(x_col)
    y_unit = get_unit(y_col)

    hover_template = (
        f"<span style='font-weight:bold'>{x_col}</span>: %{x:.2f}{x_unit}<br>"
        f"<span style='font-weight:bold'>{y_col}</span>: %{y:.2f}{y_unit}<br>"
        "<extra></extra>"
    )
    return hover_template

def get_scatterplotchartforenergy_hover_template(x_col):
    '''
        Sets the template for the hover tooltips in scatter plots for energy data.

        Parameters:
            x_col (str): The name of the x-axis column.

        Returns:
            str: The content of the tooltip.
    '''
    templates = {
        'Temperature': (
            '<b>Date</b>: %{customdata}<br>'
            '<b>Temperature</b>: %{x:.2f}ºC<br>'
            '<b>Power Consumption</b>: %{y:.2f} W<br>'
            '<extra></extra>'
        ),
        'Humidity': (
            '<b>Date</b>: %{customdata}<br>'
            '<b>Humidity</b>: %{x:.2f}%<br>'
            '<b>Power Consumption</b>: %{y:.2f} W<br>'
            '<extra></extra>'
        ),
        'WindSpeed': (
            '<b>Date</b>: %{customdata}<br>'
            '<b>Wind Speed</b>: %{x:.2f} m/s<br>'
            '<b>Power Consumption</b>: %{y:.2f} W<br>'
            '<extra></extra>'
        )
    }
    return templates.get(x_col, '')

