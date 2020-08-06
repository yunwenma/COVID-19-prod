import numpy as np
from statistics import mean 

'''
Stages of individuals in SEIR model:
     0 SUSCEPTIBLE
     1 EXPOSED
     2 INFECTED_1
     3 INFECTED_2
     4 INFECTED_3
     5 RECOVERY
     6 DEATH
'''

'''
Initial parameters
'''


# Spreading period length
SPREAD_DURATION = 100

# Initial population of each stage
INFECTED_2_0 = 0
INFECTED_3_0 = 0

EXPOSED_0 = 0 # initial exposed population
RECOVERY_0 = 0 # initial recoveried population
DEATH_0 = 0 # initial death population

'''
Clinical parameters
'''

# Duration parameters
INCUBATION_PERIOD_MEAN = 4.6 
INCUBATION_PERIOD_SD = 4.4
INCUBATION_PERIOD = mean(np.random.normal(INCUBATION_PERIOD_MEAN, INCUBATION_PERIOD_SD,1000))

# duration of incubation period
MILD_PERIOD = 6 # duration of mild infection
OBVIOUS_PERIOD = 6 # duration of obvious infection
CRITICAL_PERIOD = 8 # duration of critical infection

PERCENT_CRITICAL = 0.05 # Percentage of critical cases in all cases confirmed
PERCENT_OBVIOUS = 0.15 # Percentage of obvious cases in all cases confirmed
PERCENT_MILD = 1 - PERCENT_CRITICAL - PERCENT_OBVIOUS # Percentage of mild cases in all cases confirmed

PERCENT_DEATH = 0.4 # Percentage of death given critical cases
CASE_DEATH_RATIO = PERCENT_DEATH * PERCENT_CRITICAL # Percentage of death cases in all cases confirmed

# Infection rate of I1, I2 and I3
beta_1 = 0.5
beta_2 = 0.1
beta_3 = 0.1

# E
alpha = 1 / INCUBATION_PERIOD # Transmission rate of E-I1

# I1 - Mild
gamma_1 = (1 / MILD_PERIOD) * PERCENT_MILD # Recovery rate of I1
pi_1 = (1 / MILD_PERIOD) - gamma_1 # Transmission rate of I1-I2

# I2 - Obvious
pi_2 = (1 / OBVIOUS_PERIOD) * PERCENT_CRITICAL / (PERCENT_OBVIOUS + PERCENT_CRITICAL) # Transmission rate of I2-I3
gamma_2 = (1 / OBVIOUS_PERIOD) - pi_2 # Recovery rate of I2

# I3 - Critical
mu = (1 / CRITICAL_PERIOD) * (CASE_DEATH_RATIO / PERCENT_CRITICAL) # Death rate
gamma_3 = (1 / CRITICAL_PERIOD) - mu # Recovery rate of I3


'''
Medicare parameter
'''

HOPITAL_BED_RATIO = 2.8 # On average, number of hospital bed per 1000 individuals own
HOSPITAL_OCCUPY_RATE_INIT = 0.66 # Initial occupancy rate

ICU_BED_RATIO = 0.26 # On average, number of ICU bed per 1000 individuals own
ICU_OCCUPY_RATE_INIT = 0.68 # Initial occupancy rate

# BED_NUM = POPULATION * HOPITAL_BED_RATIO 
HOSPITAL_DURATION = OBVIOUS_PERIOD # Time of hospital stay of obvious cases
ICU_DURATION = CRITICAL_PERIOD # Time of ICU stay of critial cases
