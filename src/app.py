
# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: 
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
'''

import dash
import dash_html_components as html
import dash_core_components as dcc

import globals

import plotly.graph_objects as go
import lineChart as lc
import HeatMap as hm
import ScatterPlotChart as spc
import BarChart as bc
import BubblePlot as bp
import clusteredBarChart as cbc
import callback as cb

from dash.dependencies import Input, Output, State
from globals import df, df_daily, df_hourly


# Initialize the Dash app
app = dash.Dash(__name__)
app.title = 'Final Project | INF8808'

# Generate figures
fig_line_chart = lc.get_line_data(df_daily)
fig_heatmap_zone1 = hm.get_heatmap(df_daily, 'PowerConsumption_Zone1', 'Zone 1')
fig_heatmap_zone2 = hm.get_heatmap(df_daily, 'PowerConsumption_Zone2', 'Zone 2')
fig_heatmap_zone3 = hm.get_heatmap(df_daily, 'PowerConsumption_Zone3', 'Zone 3')
fig_heatmap_all_zones = hm.get_heatmap(df_daily, 'PowerConsumption_AllZones', 'All Zones')
fig_scatter_3zones = spc.get_ScatterPlotChart_3Zones()

# Lists of static figures
static_figures_before_line_chart = [fig_line_chart]
static_figures_before_heatmap = [fig_heatmap_zone1, fig_heatmap_zone2, fig_heatmap_zone3]
static_figures_after_heatmap = [fig_scatter_3zones]

# Layout of the Dash app
app.layout = html.Div(
    className='content',
    style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'width': '100vw',
        'height': '100vh',
        'padding': '20px',
        'textAlign': 'center',
    },
    children=[
        # Header section
        html.Header(
            style={
                'textAlign': 'center',
                'width': '100%',
                'maxWidth': '1200px'
            },
            children=[
                html.H1('Electric Power Consumption'),
                html.H2('in Tetouan (Morocco)')
            ]
        ),

        # Navigation menu
        html.Nav(
            style={
                'marginBottom': '20px',
                'width': '100%',
                'maxWidth': '1200px',
                'display': 'flex',
                'justifyContent': 'center',
                'gap': '20px'
            },
            children=[
                html.A('The Trends of Energy Consumption', href='#explanation-line-chart', className='nav-link'),
                html.A('Daily and Hourly Energy Consumption', href='#Daily-and-Hourly-Energy-Consumption', className='nav-link'),
                html.A('Electricity consumption percentage per zone', href='#Electricity-consumption-percentage', className='nav-link'),
                html.A('The Weather Condition Parameters', href='#Weather-Condition-Parameters', className = 'nav-link'),
                html.A('Impact of weather on energy consumption', href='#Impact-weather-on-energy-consumption', className='nav-link'),
                html.A('Correlation of Six Parameters: Weather Conditions and Zones', href='#Correlation-of-Six-Parameters', className = 'nav-link'),
            ]
        ),
        # Explanation before the figures
        html.Div(
            children=[
                html.Div(
                    id='explanation-line-chart',
                    style={
                        'width': '95%',
                        'maxWidth': '1200px',
                        'margin': '20px 0',
                        'textAlign': 'left'  # Align text center for better presentation
                    },
                    children=[
                        html.H2("The Trends of Energy Consumption "),
                        html.P("This visualization corresponds to a line chart, displaying the daily consumed energy values for each zone separately. The x-axis represents the date (from January 1, 2017, to December 30, 2017), while the y-axis indicates the energy quantities. Each zone's energy consumption is depicted by a distinct line and color. Additionally, the total daily consumed energy for all three zones is shown by another line in the figure for the year 2017. The legend is provided to indicate the colors used for each zone. "),
                    ],
                ),
                html.Div(
                    id='static-figures-2',
                    style={
                        'display': 'flex',
                        'flexDirection': 'column',
                        'alignItems': 'center',
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px 0'
                    },
                    children=[
                        dcc.Graph(
                            id=f'graph-before-heatmap',
                            className='graph',
                            style={
                                'width': '100%',
                                'margin': '10px 0',
                                'maxWidth': '1200px'
                            },
                            figure=fig_line_chart,
                            config={
                                'scrollZoom': False,
                                'showTips': False,
                                'showAxisDragHandles': False,
                                'doubleClick': False,
                                'displayModeBar': False
                            }
                        )
                    ]
                ),
            ]
        ),
        html.Div(
            children=[
                html.Div(
                    id='Daily-and-Hourly-Energy-Consumption',
                    style={
                        'width': '95%',
                        'maxWidth': '1200px',
                        'margin': '20px 0',
                        'textAlign': 'left'  # Align text center for better presentation
                    },
                    children=[
                        html.H2("Daily and Hourly Energy Consumption"),
                        html.P("We visualize the energy consumption of each zone through a set of heatmaps, where each box represents a day of the year. The x-axis spans the months of the year from January to December, while the y-axis indicates the days of the week from Monday to Sunday. Each heatmap is labeled to show the energy consumption specific to the corresponding zone, and an additional heatmap aggregates the power consumption of all zones. A legend is included to explain the color scheme used in the heatmaps. This collection of heatmaps provides users with insights into the daily, weekly, monthly, and zone-specific variations in electricity usage. "),
                    ]
                ),

                html.Div(
                    id='static-figures',
                    style={
                        'display': 'flex',
                        'flexDirection': 'column',
                        'alignItems': 'center',
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px 0'
                    },
                    children=[
                        dcc.Graph(
                            id=f'graph-before-heatmap-{i}',
                            className='graph',
                            style={
                                'width': '100%',
                                'margin': '10px 0',
                                'maxWidth': '1200px'
                            },
                            figure=fig,
                            config={
                                'scrollZoom': False,
                                'showTips': False,
                                'showAxisDragHandles': False,
                                'doubleClick': False,
                                'displayModeBar': False
                            }
                        ) for i, fig in enumerate(static_figures_before_heatmap)
                    ]
                ),
            ]
        ),

        # Flexbox container for heatmap and bar chart
        html.Div(
            children=[
                html.Div(
                    id='explanation-before-heatmap-bar',
                    style={
                        'width': '95%',
                        'maxWidth': '1200px',
                        'margin': '20px 0',
                        'textAlign': 'left'  # Align text center for better presentation
                    },
                    children=[
                        html.P("In this heat map, by clicking on each rectangle reveals a panel containing a bar chart. This bar chart depicts the hourly maximum energy usage for the chosen day, with the x-axis showing the hour number (1 to 24) and the y-axis representing the consumed quantity of energy. "),
                    ]
                ),

                html.Div(
                    id='heatmap-bar',
                    className='heatmap-bar-container',
                    style={
                        'display': 'flex',
                        'flexDirection': 'row',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'width': '100%',
                        'maxWidth': '1200px',
                        'height': '500px',
                        'margin': '20px 0',
                        'gap': '20px'
                    },
                    children=[
                        # Heatmap graph
                        dcc.Graph(
                            id='heatmap',
                            className='graph',
                            style={
                                'flex': '0 0 70%',
                                'minWidth': '0',
                                'margin': 'auto'
                            },
                            figure=fig_heatmap_all_zones,
                            config={
                                'scrollZoom': False,
                                'showTips': False,
                                'showAxisDragHandles': False,
                                'doubleClick': False,
                                'displayModeBar': False
                            }
                        ),
                        # Bar chart panel, initially hidden
                        html.Div(
                            id='bar-chart-panel',
                            className='panel-div',
                            style={
                                'visibility': 'hidden',
                                'flex': '0 0 30%',
                                'minWidth': '0',
                                'margin': 'auto',
                                'display': 'flex',
                                'alignItems': 'center',
                                'justifyContent': 'center'
                            },
                            children=[
                                dcc.Graph(
                                    id='bar-chart',
                                    config={
                                        'displayModeBar': False,
                                        'scrollZoom': False,
                                        'showTips': False,
                                        'showAxisDragHandles': False,
                                        'doubleClick': False
                                    }
                                )
                            ]
                        )
                    ]
                ),
            ]
        ),

        #  Stacked bar chart and clustered bar chart
        html.Div(
            children=[
                html.Div(
                    id='Electricity-consumption-percentage',
                    style={
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px 0',
                        'textAlign': 'left'  # Align text center for better presentation
                    },
                    children=[
                        html.H2("Electricity consumption percentage per zone "),
                        html.P("This part facilitates a clearer comparison between different zones. In Clustered bar chart, the x-axis represents the zone names, while the y-axis displays the power consumption values. Each zone is represented by a separate bar, and the percentage of each zone can be displayed on its corresponding bar. This visualization method provides an easy way for users to understand the distribution of electricity consumption across different zones. Additionally, a checkbox panel on the left side of the chart allows users to select one or multiple months, enabling them to observe the proportion of each zone's consumption for the chosen months. We offer users a detailed breakdown of each zone's proportion within selected months using a stacked bar chart. In this chart, the x-axis represents the month names, and the y-axis represents the power consumption quantities. Each bar in the chart illustrates the percentage of each zone within each month. ")
                    ]
                ),

                html.Div(
                    id='stacked-bar-charts',
                    style={
                        'display': 'flex',
                        'flexDirection': 'row',
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px 0'
                    },
                    children=[
                        html.Div(
                            style={
                                'width': '20%',
                                'padding': '10px',
                                'display': 'flex',
                                'flexDirection': 'column',
                                'justifyContent': 'flex-start'
                            },
                            children=[
                                dcc.Checklist(
                                    id='month-checklist',
                                    options=[{'label': month, 'value': month} for month in
                                             ["January", "February", "March", "April",
                                              "May", "June", "July", "August",
                                              "September", "October", "November",
                                              "December"]],
                                    value=[],  # No months selected by default
                                    labelStyle={'display': 'block'}
                                ),
                                html.Button('Update Chart', id='update-button', n_clicks=0, style={'marginTop': '10px'})
                            ]
                        ),
                        html.Div(
                            style={
                                'width': '80%',
                                'padding': '10px'
                            },
                            children=[
                                dcc.Graph(
                                    id='stacked-bar-chart',
                                    style={'width': '100%', 'height': '400px'},  # Adjusted height
                                    config={
                                        'scrollZoom': False,
                                        'showTips': False,
                                        'showAxisDragHandles': False,
                                        'doubleClick': False,
                                        'displayModeBar': False
                                    }
                                ),
                                dcc.Graph(
                                    id='stacked-bar-chart-2',
                                    style={'width': '100%', 'height': '400px'},  # Adjusted height
                                    config={
                                        'scrollZoom': False,
                                        'showTips': False,
                                        'showAxisDragHandles': False,
                                        'doubleClick': False,
                                        'displayModeBar': False
                                    }
                                )
                            ]
                        )
                    ]
                ),
            ]
        ),

        # a scatter plot charts
        html.Div(
            children=[
                html.Div(
                    id='Weather-Condition-Parameters',
                    style={
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px auto',
                        'textAlign': 'left'  # Align text center for better presentation
                    },
                    children=[
                        html.H2("The Weather Condition Parameters "),
                        html.P("This part, a scatter plot charts, provides insights into weather conditions (temperature, humidity, wind speed) by allowing users to visualize the correlations among different weather variables. Each plot displays data points (represented by small circles) positioned along quantitative x- and y-axes, with the x-axis and y-axis representing two of the three weather condition parameters. the user is provided with two combo boxes, allowing them to select one of three weather condition parameters for each axis. Upon selecting the parameters, the scatter plot updates to show the chosen parameters on the x and y axes, along with the corresponding data points. ")
                    ]
                ),

                html.Div(
                    id='dynamic-plots',
                    className='dropdown-container',
                    style={
                        'display': 'flex',
                        'justifyContent': 'space-around',
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px auto'
                    },
                    children=[
                        dcc.Dropdown(
                            id='x-column-dropdown',
                            options=[
                                {'label': 'Humidity', 'value': 'Humidity'},
                                {'label': 'Temperature', 'value': 'Temperature'},
                                {'label': 'WindSpeed', 'value': 'WindSpeed'}
                            ],
                            value='Humidity',  # Default value
                            placeholder="Select X-axis column",
                            style={'width': '45%'}
                        ),
                        dcc.Dropdown(
                            id='y-column-dropdown',
                            options=[
                                {'label': 'Humidity', 'value': 'Humidity'},
                                {'label': 'Temperature', 'value': 'Temperature'},
                                {'label': 'WindSpeed', 'value': 'WindSpeed'}
                            ],
                            value='WindSpeed',  # Default value
                            placeholder="Select Y-axis column",
                            style={'width': '45%'}
                        )
                    ]
                ),
            ]
        ),
        # Placeholders for dynamic scatter plot and bubble plot
        html.Div(
            id='dynamic-scatter',
            style={
                'width': '100%',
                'maxWidth': '1200px',
                'margin': '20px 0',
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center'
            },
            children=[
                dcc.Graph(
                    id='dynamic-scatter-plot',
                    style={'width': '100%', 'height': '100%'},
                    config={
                        'scrollZoom': False,
                        'showTips': False,
                        'showAxisDragHandles': False,
                        'doubleClick': False,
                        'displayModeBar': False
                    }
                )
            ]
        ),
        # Dropdowns for selecting columns for dynamic plots
        html.Div(
            children=[
                html.Div(
                    id='Impact-weather-on-energy-consumption',
                    style={
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px auto',
                        'textAlign': 'left'  # Align text to the left for better readability
                    },
                    children=[
                        html.H2("Impact of weather on energy consumption "),
                        html.P("This visualization, comprising a bubble plot, provides insights into how weather conditions impact electricity usage. It allows users to visually assess the influence of different weather variables—specifically temperature, humidity, and wind speed—on power consumption. This plot features two meteorological variables on the x and y axes. To depict the relationship between weather parameters and power consumption, the plots use circles of varying sizes, with the size representing energy quantity. Given the relatively small differences in energy consumption, colors are utilized to accentuate these distinctions. Each bubble corresponds to a day in the year 2017, with the bubble's size indicating the total energy consumption for that particular day. Users can select two weather parameters, after which the bubble plot axes adjust accordingly. Subsequently, the bubbles on the plot update to reflect electricity usage. ")
                    ]
                ),

                html.Div(
                    id='dynamic-plots-1',
                    className='dropdown-container',
                    style={
                        'display': 'flex',
                        'justifyContent': 'space-around',
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px auto',
                        'alignItems': 'left'  # Align dropdowns to the left
                    },
                    children=[
                        dcc.Dropdown(
                            id='x-column-dropdown-1',
                            options=[
                                {'label': 'Humidity', 'value': 'Humidity'},
                                {'label': 'Temperature', 'value': 'Temperature'},
                                {'label': 'WindSpeed', 'value': 'WindSpeed'}
                            ],
                            value='Humidity',  # Default value
                            placeholder="Select X-axis column",
                            style={'width': '45%'}
                        ),
                        dcc.Dropdown(
                            id='y-column-dropdown-1',
                            options=[
                                {'label': 'Humidity', 'value': 'Humidity'},
                                {'label': 'Temperature', 'value': 'Temperature'},
                                {'label': 'WindSpeed', 'value': 'WindSpeed'}
                            ],
                            value='WindSpeed',  # Default value
                            placeholder="Select Y-axis column",
                            style={'width': '45%'}
                        )
                    ]
                ),
            ]
        ),
        # Bubble Scatter
        html.Div(
            id='dynamic-bubble',
            style={
                'width': '100%',
                'maxWidth': '1200px',
                'margin': '20px 0',
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center'
            },
            children=[
                dcc.Graph(
                    id='dynamic-bubble-plot',
                    style={'width': '100%', 'height': '100%'},
                    config={
                        'scrollZoom': False,
                        'showTips': False,
                        'showAxisDragHandles': False,
                        'doubleClick': False,
                        'displayModeBar': False
                    }
                )
            ]
        ),


        # Dropdowns for selecting columns for dynamic plots
        html.Div(
            children=[
                html.Div(
                    id='Correlation-of-Six-Parameters',
                    style={
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px auto',
                        'textAlign': 'left'  # Align text center for better presentation
                    },
                    children=[
                        html.H2("Correlation of Six Parameters: Weather Conditions and Zones"),
                        html.P("The final visualization comprises scatter plot charts that offer insights into how weather conditions (temperature, humidity, wind speed) affect the energy usage of different zones separately. Each chart showcases data points (depicted as small circles) placed along quantitative x- and y-axes. The x-axis corresponds to one of the weather condition parameters, while the y-axis represents the energy values of three distinct zones. The points' colors are associated with the respective zones, with a legend included to clarify the color scheme.   ")
                    ]
                ),

                html.Div(
                    id='dynamic-plots-2',
                    className='dropdown-container',
                    style={
                        'display': 'flex',
                        'justifyContent': 'space-around',
                        'width': '100%',
                        'maxWidth': '1200px',
                        'margin': '20px auto'
                    },
                    children=[
                        dcc.Dropdown(
                            id='x-column-dropdown-2',
                            options=[
                                {'label': 'Humidity', 'value': 'Humidity'},
                                {'label': 'Temperature', 'value': 'Temperature'},
                                {'label': 'WindSpeed', 'value': 'WindSpeed'}
                            ],
                            value='Humidity',  # Default value
                            placeholder="Select X-axis column",
                            style={'width': '45%'}
                        )
                    ]
                ),
            ]
        ),
        html.Div(
            id='dynamic-scatter-3zones',
            style={
                'width': '100%',
                'maxWidth': '1200px',
                'margin': '20px 0',
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center'
            },
            children=[
                dcc.Graph(
                    id='dynamic-scatter-3zones-plot',
                    style={'width': '100%', 'height': '100%'},
                    config={
                        'scrollZoom': False,
                        'showTips': False,
                        'showAxisDragHandles': False,
                        'doubleClick': False,
                        'displayModeBar': False
                    }
                )
            ]
        ),
        html.Div([
            html.Button("Scroll Up", id="scroll-to-top", n_clicks=0, style={
                'position': 'fixed',
                'bottom': '20px',
                'right': '20px',
                'padding': '20px 40px',
                'background-color': '#007bff',
                'color': 'white',
                'border': 'none',
                'border-radius': '5px',
                'cursor': 'pointer',
                'font-size': '20px',
                'font-family': 'Arial, sans-serif',
                'z-index': '1000'
            })
        ]),
    ]
)

# JavaScript to scroll to top
app.clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks > 0) {
            window.scrollTo({top: 0, behavior: 'smooth'});
        }
        return '';
    }
    """,
    dash.dependencies.Output('scroll-to-top', 'children'),
    [dash.dependencies.Input('scroll-to-top', 'n_clicks')]
)

@app.callback(
    [Output('stacked-bar-chart', 'figure'),
     Output('stacked-bar-chart-2', 'figure')],
    [Input('update-button', 'n_clicks')],
    [State('month-checklist', 'value')]
)
def update_chart(n_clicks, selected_months):
    selected_months = selected_months
    if n_clicks > 0:  # Check if the button has been clicked
        return cbc.get_clustered_bar_chart_zone(selected_months), cbc.get_stacked_bar_chart_month(selected_months)
    else:
        return go.Figure(), go.Figure()  # Return an empty figure initially


@app.callback(
    Output('dynamic-scatter-3zones-plot', 'figure'),
    Input('x-column-dropdown-2', 'value')
)
def update_scatter_plot_3zones(x_column):
    if x_column:
        print(x_column)
        fig = spc.get_ScatterPlotChart_3Zones(x_col=x_column)
        return fig
    return {}


@app.callback(
    [Output('bar-chart', 'figure'),
     Output('bar-chart-panel', 'style')],
    Input('heatmap', 'clickData')
)
def update_bar_chart(click_data):
    if click_data:
        date_clicked = cb.get_date_from_click(click_data)  # Extract date information
        fig_bar_chart = bc.get_bar_chart(df_hourly, date_clicked)
        fig_bar_chart.update_layout(dragmode='pan')
        fig_bar_chart.update_layout(
            xaxis=dict(fixedrange=True),
            yaxis=dict(fixedrange=True)
        )
        return fig_bar_chart, {'visibility': 'visible', 'padding': '10px', 'width': '80%', 'margin': 'auto'}
    return {}, {'visibility': 'hidden'}


@app.callback(
    Output('dynamic-scatter-plot', 'figure'),
    [Input('x-column-dropdown', 'value'), Input('y-column-dropdown', 'value')]
)


def update_scatter_plot(x_column, y_column):
    if x_column and y_column:
        return spc.get_ScatterPlotChart(df_hourly, x_column, y_column)
    return {}


@app.callback(
    Output('dynamic-bubble-plot', 'figure'),
    [Input('x-column-dropdown-1', 'value'), Input('y-column-dropdown-1', 'value')]
)
def update_bubble_plot(x_column, y_column):
    if x_column and y_column:
        return bp.get_bubble_plot(df_daily, x_column, y_column)
    return {}