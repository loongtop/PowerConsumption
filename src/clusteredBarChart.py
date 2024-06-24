import pandas as pd
import preprocess as pp
import plotly.express as px

from globals import df


# Function to update the stacked bar chart
def update_stacked_bar_chart_zone(DailyData_df, selected_months):

    # Filter the DataFrame based on selected months
    filtered_df = DailyData_df[DailyData_df['MonthName'].isin(selected_months)]

    # Sum the power consumption for each zone
    zone_sums = filtered_df[['Zone1', 'Zone2', 'Zone3']].sum().reset_index()
    zone_sums.columns = ['Zone', 'PowerConsumption']

    # Calculate the percentage of each zone from the whole zones
    zone_sums['Percentage'] = zone_sums['PowerConsumption'] / zone_sums['PowerConsumption'].sum() * 100
    zone_sums['Percentage'] = zone_sums['Percentage'].apply(
        lambda x: '{:.2f}%'.format(x))  # Format to two decimal places

    # Define a color sequence suitable for color blindness
    color_sequence = ['#1f77b4', '#ff7f0e', '#2ca02c']

    # Create a stacked bar chart with Plotly
    fig = px.bar(zone_sums, x='Zone', y='PowerConsumption', title='Proportion of Power Consumption by Zone',
                 color='Zone', text='Percentage', color_discrete_sequence=color_sequence,
                 hover_data={'PowerConsumption': True, 'Percentage': False},
                 labels={'PowerConsumption': 'Power Consumption (kWh)'})

    # Update layout for better readability
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})

    # Increase the font size of the bar chart labels
    fig.update_layout(font=dict(size=14), xaxis_title=None)

    return fig


def get_clustered_bar_chart_zone(selected_months):

    # Columns to average and to find the maximum
    columns_to_avg = ['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows']
    columns_to_max = ['Zone1', 'Zone2', 'Zone3', 'PowerConsumption_AllZones']

    # Group by specified columns and aggregate
    DailyData_df = df.groupby(['date', 'week', 'DayName', 'MonthName', 'MonthNumber', 'DayOfMonth', 'DayOfYear']).agg(
        {**{col: 'mean' for col in columns_to_avg}, **{col: 'max' for col in columns_to_max}}
    ).reset_index()

    return update_stacked_bar_chart_zone(DailyData_df, selected_months)


def update_stacked_bar_chart_month(DailyData_df, selected_months):

    # Filter the DataFrame based on selected months
    filtered_df = DailyData_df[DailyData_df['MonthName'].isin(selected_months)]

    # Calculate the total power consumption for each zone and each month
    monthly_consumption = filtered_df.groupby('MonthName')[['Zone1', 'Zone2', 'Zone3']].sum().reset_index()

    # Calculate the percentages
    monthly_consumption['Total'] = monthly_consumption[['Zone1', 'Zone2', 'Zone3']].sum(axis=1)
    monthly_consumption['Zone1_pct'] = (monthly_consumption['Zone1'] / monthly_consumption['Total']) * 100
    monthly_consumption['Zone2_pct'] = (monthly_consumption['Zone2'] / monthly_consumption['Total']) * 100
    monthly_consumption['Zone3_pct'] = (monthly_consumption['Zone3'] / monthly_consumption['Total']) * 100

    # Melt the DataFrame for plotting
    melted_df = monthly_consumption.melt(id_vars='MonthName', value_vars=['Zone1', 'Zone2', 'Zone3'],
                                         var_name='Zone', value_name='PowerConsumption')
    melted_df['Percentage'] = melted_df.apply(lambda row:
                                              (row['PowerConsumption'] / monthly_consumption[
                                                  monthly_consumption['MonthName'] == row['MonthName']][
                                                  'Total'].values[0]) * 100, axis=1)

    # Define a color sequence suitable for color blindness
    color_sequence = ['#1f77b4', '#ff7f0e', '#2ca02c']

    # Ensure 'MonthName' is categorical and ordered correctly
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']

    melted_df['MonthName'] = pd.Categorical(melted_df['MonthName'], categories=month_order, ordered=True)

    # Now, plot the sorted data
    fig = px.bar(melted_df.sort_values(by='MonthName'),  # Sort by 'MonthName'
                 x='MonthName', y='PowerConsumption', color='Zone',
                 title='Proportion of Power Consumption by Month',
                 color_discrete_sequence=color_sequence, text='Percentage',
                 hover_data={'PowerConsumption': True, 'Percentage': ':.2f'})

    # Update layout for better readability
    fig.update_layout(barmode='stack', xaxis_title=None)

    # Update text template for percentage display
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='inside')

    # Increase the font size of the bar chart labels
    fig.update_layout(font=dict(size=14))

    return fig


def get_stacked_bar_chart_month(selected_months):
    # Columns to average and to find the maximum
    columns_to_avg = ['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows']
    columns_to_max = ['Zone1', 'Zone2', 'Zone3', 'PowerConsumption_AllZones']

    # Group by specified columns and aggregate
    DailyData_df = df.groupby(['date', 'week', 'DayName', 'MonthName', 'MonthNumber', 'DayOfMonth', 'DayOfYear']).agg(
        {**{col: 'mean' for col in columns_to_avg}, **{col: 'max' for col in columns_to_max}}
    ).reset_index()

    return update_stacked_bar_chart_month(DailyData_df, selected_months)

