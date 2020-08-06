import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from parameter import *
from SEIR import SEIR
from status_curve import * # import fig_curve - The number of individuals in different stage of COVID-19 (SEIR output)
from crowd import * # import fig_crowd: The spreading situation in crowd
from medicare import * # import fig_medicare: The hospital bed occupation condition

app = dash.Dash()

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

'''
Web App Layout Design
'''

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='The Dashboard of COVID-19 Spreading Simulation',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Developed by Yunwen Ma', style={
        'textAlign': 'center',
        'color': colors['text']
        }
    ),
    html.Div([
        # Input 1 - total population
        html.P("Type in the population and the initial infectious case number:"),
        dcc.Input(id="input1", type="text", placeholder="Population", value=100, min=20, max=10000, step=1),
        # Input 2 - initial infectious case number
        dcc.Input(id="input2", type="text", placeholder="Initial Infectious case", value = 1, min=0, max=100, step=1, debounce=True), 
        html.Br(),     
        # Input 3.... 
        ]
    ),
    html.Div(id = "output"),
    # Add fig_curve
    dcc.Graph(id = 'Graph1'),
    # Add fig_crowd
    dcc.Graph(id = 'Graph2'),
    # Add fig_hospital
    dcc.Graph(id = 'Graph3')
    
])

@app.callback(
    Output("Graph1", "figure"),
    [Input("input1", "value"), Input("input2", "value")],
)
def update_graph(pop, inf_ini):
    pop = int(pop)
    inf_ini = int(inf_ini)
    SEIR_output = SEIR(pop, inf_ini).calc_SEIR()
    # import fig_curve
    fig_curve = plot_status_curve(SEIR_output)
    return fig_curve #u'The total population is {} while the initial infectious case number is {}.'.format(input1,input2)

@app.callback(
    Output("Graph2", "figure"),
    [Input("input1", "value"), Input("input2", "value")],
)
def update_graph(pop, inf_ini):
    pop = int(pop)
    inf_ini = int(inf_ini)
    SEIR_output = SEIR(pop, inf_ini).calc_SEIR()  
    # import fig_crowd
    fig_crowd = plot_crowd(SEIR_output,pop)
    return fig_crowd
 
@app.callback(
    Output("Graph3", "figure"),
    [Input("input1", "value"), Input("input2", "value")], 
)
def update_graph(pop, inf_ini):
    pop = int(pop)
    inf_ini = int(inf_ini)
    SEIR_output = SEIR(pop, inf_ini).calc_SEIR()
    # import fig_medicare
    fig_medicare = plot_medicare(SEIR_output, pop)
    return fig_medicare

if __name__ == '__main__':
    app.run_server(debug=True)