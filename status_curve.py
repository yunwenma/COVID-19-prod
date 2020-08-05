import plotly.graph_objects as go

from parameter import *
from SEIR import SEIR

# Fig_curve: The number of individuals in different stage of COVID-19 (SEIR output)

def plot_status_curve(SEIR_output):
     #Create figures for the model output
     trace1 = go.Scatter(x=SEIR_output.index,
                         y=SEIR_output['S'],
                         mode='lines',
                         name='Susceptible',
                         line=dict(width=1.5))

     trace2 = go.Scatter(x = SEIR_output.index,
                         y = SEIR_output['E'],
                         mode='lines',
                         name='Exposed',
                         line=dict(width=1.5))

     trace3 = go.Scatter(x = SEIR_output.index,
                         y = SEIR_output['I1'],
                         mode='lines',
                         name='Mildly Infectious',
                         line=dict(width=1.5))

     trace4 = go.Scatter(x = SEIR_output.index,
                         y = SEIR_output['I2'],
                         mode='lines',
                         name='Obviously Infectious',
                         line=dict(width=1.5))

     trace5 = go.Scatter(x = SEIR_output.index,
                         y = SEIR_output['I3'],
                         mode='lines',
                         name='Critically Infectious',
                         line=dict(width=1.5))

     trace6 = go.Scatter(x = SEIR_output.index,
                         y = SEIR_output['R'],
                         mode='lines',
                         name='Recovered',
                         line=dict(width=1.5))

     trace7 = go.Scatter(x = SEIR_output.index,
                         y = SEIR_output['D'],
                         mode='lines',
                         name='Dead',
                         line=dict(width=1.5))

     frames = [dict(data= [dict(type='scatter',
                              x=SEIR_output.index[:k+1],
                              y=SEIR_output['S'][:k+1]),
                         dict(type='scatter',
                              x=SEIR_output.index[:k+1],
                              y=SEIR_output['E'][:k+1]),
                         dict(type='scatter',
                              x=SEIR_output.index[:k+1],
                              y=SEIR_output['I1'][:k+1]),
                         dict(type='scatter',
                              x=SEIR_output.index[:k+1],
                              y=SEIR_output['I2'][:k+1]),
                         dict(type='scatter',
                              x=SEIR_output.index[:k+1],
                              y=SEIR_output['I3'][:k+1]),
                         dict(type='scatter',
                              x=SEIR_output.index[:k+1],
                              y=SEIR_output['R'][:k+1]),
                         dict(type='scatter',
                              x=SEIR_output.index[:k+1],
                              y=SEIR_output['D'][:k+1])
                         ],
                    traces= [0, 1, 2, 3, 4, 5, 6],  
               )for k in range(SEIR_output.shape[0])] 

     layout = go.Layout(showlegend=True,
                    hovermode='x unified',
                    updatemenus=[
                         dict(
                              type='buttons', showactive=False,
                              y=1.05,
                              x=1.15,
                              xanchor='right',
                              yanchor='top',
                              pad=dict(t=0, r=10),
                              buttons=[dict(label='Play',
                              method='animate',
                              args=[None, 
                                   dict(frame=dict(duration=3, 
                                                       redraw=False),
                                                       transition=dict(duration=0),
                                                       fromcurrent=True,
                                                       mode='immediate')]
                              )]
                         )
                         ]              
                    )


     # Generate the figure with 7 traces
     fig_curve = go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6, trace7], frames=frames, layout=layout)

     fig_curve.update_layout(title='The number of individuals in different stage of COVID-19',
                    xaxis_title='Day',
                    yaxis_title='Case Number')
     return fig_curve