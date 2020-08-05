import numpy as np
import pandas as pd
import plotly.express as px

from parameter import *
from SEIR import SEIR

def plot_crowd(SEIR_output, population):
    # Convert the case number of each stage into the % of each stage
    SEIR_div = SEIR_output.div(SEIR_output.sum(axis=1), axis=0)

    # Create the rondom data set
    randomlist_x = []
    randomlist_y = []

    num_random = population
    init_point = (0, 0)

    for i in range(0,num_random):
        x = np.random.normal(0, 1) + init_point[0]
        y = np.random.normal(0, 1) + init_point[1]  
        randomlist_x.append(x)
        randomlist_y.append(y)

    dot_position = pd.DataFrame({'x': randomlist_x, 'y':randomlist_y})

    # Create a new table for all position and all possible status
    dot_position_time = pd.DataFrame()

    # Generate the dataframe for all dots' status change over time
    for z in range(0, dot_position.shape[0]):
        dot_position_spe = dot_position.iloc[[z]]
        randomlist_status = []

        for j in range(0,SEIR_div.shape[0]):
            status = np.random.choice(list(SEIR_div.columns), p=list(SEIR_div.loc[j,]))
            randomlist_status.append(status)
        
        dot_position_spe = pd.concat([dot_position_spe]*len(randomlist_status), ignore_index=True)
        dot_position_spe['status'] = randomlist_status
        dot_position_time = pd.concat([dot_position_time , dot_position_spe], ignore_index=True)
   
    dot_position_time['time'] = list(range(SPREAD_DURATION+1))*population

    fig_crowd = px.scatter(dot_position_time, x="x", y="y", color="status",  
                            animation_frame="time") #animation_group="country"

    # Remove axes
    fig_crowd.update_xaxes(visible=False, fixedrange=True)
    fig_crowd.update_yaxes(visible=False, fixedrange=True)
    fig_crowd.update_layout(annotations=[], overwrite=True)

    fig_crowd.update_layout(title='COVID-19 Spreading Status in crowds')

    return fig_crowd
