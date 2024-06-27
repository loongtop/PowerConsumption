'''
    File name: callback.py
    Purpose: Contains callback functions for handling interactions in the Dash app.
    Authors:
        - Yuashun Cui - 2404877
        - Samira Nazari - 2310647
        - Mohamad Hadi Ajami - 2227105
    Course: INF8808
    Python Version: 3.8

    This file provides the functionality to process user interactions and update the app's visualizations.
'''

from datetime import datetime, timedelta


# Function to map click data to a specific date
def get_date_from_click(click_data):
    """
    Convert heatmap click data to a date.

    Parameters:
        click_data (dict): Data from a heatmap click event.

    Returns:
        str: Date string in the format 'YYYY-MM-DD' or None if click_data is invalid.
    """
    # Map of day names to integers
    day_map = {
        'Sunday': 0,
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6
    }

    # Check if click data is valid
    if click_data and 'points' in click_data:
        point = click_data['points'][0]
        week_of_year = point['x']
        day_of_week = point['y']

        # Map day name to integer
        day_of_week_index = day_map[day_of_week]

        # Start date for 2017
        start_date = datetime.strptime('2017-01-01', '%Y-%m-%d')

        # Calculate the first day of the specified week
        days_to_add = (week_of_year - 1) * 7 + day_of_week_index  # week_of_year - 1 because weeks are 0-indexed
        specific_date = start_date + timedelta(days=days_to_add)

        return specific_date.strftime('%Y-%m-%d')
    
    return None