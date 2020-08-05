import numpy as np
import pandas as pd
import scipy.integrate as spi

from parameter import *

class SEIR(object):
    def __init__(self, POPULATION, INFECTED_1_0):
        # List of initial values
        self.population = POPULATION
        self.infected_1_0 = INFECTED_1_0
        self.susceptible_0 = self.population - self.infected_1_0 - INFECTED_2_0 - INFECTED_3_0 - EXPOSED_0 - RECOVERY_0 # initial susceptible population
        self.initial_list = (self.susceptible_0,EXPOSED_0,self.infected_1_0,INFECTED_2_0,INFECTED_3_0,RECOVERY_0,DEATH_0)
        self.spread_duration = SPREAD_DURATION       

    # Define the class transmission function
    def df_SEIR(self,initial_list,_):
        Y = np.zeros(7)
        X = initial_list

        # Track the derivative of SEIR transmission        
        Y[0] = - (beta_1 * X[2] + beta_2 * X[3] + beta_3 * X[4]) / self.population * X[0] # Susceptible population change
        Y[1] = (beta_1 * X[2] + beta_2 * X[3] + beta_3 * X[4]) / self.population * X[0] - alpha * X[1]  # Exposed population change
        Y[2] = alpha * X[1] - (pi_1 + gamma_1) * X[2]  # Infection_1 population change
        Y[3] = pi_1 *  X[2] - (pi_2 + gamma_2) * X[3]  # Infection_2 population change
        Y[4] = pi_2 * X[3] - (mu + gamma_3) * X[4] # Infection_3 population change
        Y[5] = gamma_1 * X[2] + gamma_2 * X[3] + gamma_3 * X[4]  # Recovery population change
        Y[6] = mu * X[4]  # Death population change
        
        return Y

    # Calculate the case numbers in SEIR stages with respect to time
    def calc_SEIR(self):
        T_range = np.arange(0, self.spread_duration + 1)
        RES = spi.odeint(self.df_SEIR, self.initial_list, T_range)
        RES_df = pd.DataFrame(RES)
        RES_df.columns = list(RES_df.columns)
        RES_df = RES_df.rename(columns={0:'S', 1:'E', 2:'I1', 3:'I2', 4:'I3', 5:'R', 6:'D'})

        return RES_df

# SEIR_output = SEIR(100, 1).calc_SEIR()
# SEIR_output["sum"] = SEIR_output.sum(axis=1)
# SEIR_output.to_csv("check_data.csv")