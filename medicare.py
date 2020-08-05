import plotly.graph_objects as go

from parameter import *
from SEIR import *

def plot_medicare(SEIR_output, population):
    hospital_bed_occu_init = HOPITAL_BED_RATIO * HOSPITAL_OCCUPY_RATE_INIT * population / 1000
    icu_bed_occu_init = ICU_BED_RATIO *  ICU_OCCUPY_RATE_INIT * population / 1000

    hospital_bed_occu_rate = []
    icu_bed_occu_rate = []

    for i in range(0,SPREAD_DURATION):
        hospital_bed_occu_i = hospital_bed_occu_init + SEIR_output.at[i,'I2']
        hospital_bed_occu_rate_i = hospital_bed_occu_i / (HOPITAL_BED_RATIO * population / 1000)
        if hospital_bed_occu_rate_i <= 1:
            hospital_bed_occu_rate_i_final = hospital_bed_occu_rate_i
        else:
            hospital_bed_occu_rate_i_final = 1  

        icu_bed_occu_i = icu_bed_occu_init + SEIR_output.at[i,'I3']
        icu_bed_occu_rate_i = icu_bed_occu_i / (ICU_BED_RATIO * population / 1000)

        if icu_bed_occu_rate_i <= 1:
            icu_bed_occu_i_final = icu_bed_occu_rate_i
        else:
            icu_bed_occu_i_final = 1

        hospital_bed_occu_rate.append(hospital_bed_occu_rate_i_final)
        icu_bed_occu_rate.append(icu_bed_occu_i_final)

        
    medicare_occupy = pd.DataFrame({'time': list(range(0,SPREAD_DURATION)), 
                                 'hospital_bed_occu_rate': hospital_bed_occu_rate,
                                 'icu_bed_occu_rate': icu_bed_occu_rate})
    
    trace1 = go.Scatter(x=medicare_occupy.index,
                         y=medicare_occupy['hospital_bed_occu_rate'],
                         mode='lines',
                         name='Hospital Bed Occupation Rate',
                         line=dict(width=1.5))

    trace2 = go.Scatter(x = medicare_occupy.index,
                         y = medicare_occupy['icu_bed_occu_rate'],
                         mode='lines',
                         name='ICU Bed Occupation Rate',
                         line=dict(width=1.5))
    
    fig_medicare = go.Figure(data=[trace1, trace2])
    fig_medicare.update_layout(title='The Hospital Beds and ICU Beds Occupation Rate',
                    xaxis_title='Day',
                    yaxis_title='Occupation Rate - %')
    
    return fig_medicare

# SEIR_output = SEIR(1000, 1).calc_SEIR()
# hos_data = plot_medicare(SEIR_output, 1000)
# hos_data.show()
