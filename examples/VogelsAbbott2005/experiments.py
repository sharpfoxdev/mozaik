#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet
    

def create_experiments(model):
    
    return  [
                           #Lets kick the network up into activation
                           PoissonNetworkKick(model,duration=8*7,sheet_list=["Exc_Layer","Inh_Layer"],recording_configuration={'component' : 'mozaik.sheets.population_selector.RCRandomPercentage','params' : {'percentage' : 20.0}},lambda_list=[100.0,100.0],weight_list=[0.1,0.1]),
                           #Spontaneous Activity 
                           NoStimulation(model,duration=3*8*7),
            ]
