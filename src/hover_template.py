def get_line_chart_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip

    first_line = "<span style='font-weight:bold'>Date</span>: %{x}"
    second_line = "<span style='font-weight:bold'>Power Consumption</span>: %{y}"
    second_line += "<extra></extra>"

    return "<br>".join([first_line, second_line])


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip

    first_line = "<span style='font-weight:bold'>Week of the Year</span>: %{x}"
    second_line = "<span style='font-weight:bold'>Day of the Week</span>: %{y}"
    third_line = "<span style='font-weight:bold'>Power Consumption</span>: %{z} W"
    third_line += "<extra></extra>"

    return (
        '<b>Week</b>: %{x}<br>'
        '<b>Day of Week</b>: %{y}<br>'
        '<b>Power Consumption</b>: %{z:.2f} kW<extra></extra>'
    )
    return "<br>".join([first_line, second_line, third_line])

def get_barchart_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip

    first_line = "<span style='font-weight:bold'>Hour</span>: %{x}"
    second_line = "<span style='font-weight:bold'>Power Concumption</span>: %{y}W"
    second_line += "<extra></extra>"

    return "<br>".join([first_line, second_line])


def get_scatterplotchart_hover_template(x_col, y_col):
    '''
        Sets the template for the hover tooltips.
        
        

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip

    first_line =  f"<span style='font-weight:bold'>{x_col}"+"</span>: %{x}"
    second_line =  f"<span style='font-weight:bold'>{y_col}"+"</span>: %{y}"
    second_line += "<extra></extra>"

    return "<br>".join([first_line, second_line])

def get_scatterplotchartforenergy_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip

    return '<b>Date</b>: %{customdata}<br><b>Temperature</b>: %{x}<br><b>Power Consumption</b>: %{y}<extra></extra>'
