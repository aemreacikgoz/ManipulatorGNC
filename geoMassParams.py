import numpy as np
import matplotlib.pyplot as plt
import scipy
class Params:
    def __init__(self):
        self.definition()

    def definition(self):
        #### Initial Definitions
        # Chaser Spacecraft
        self.M_c = 15   # kg
        self.lx_c = 0.8 # m
        self.ly_c = 0.8 # m
        self.lz_c = 0.8 # m
        self.Ixx_c  = 1/12*self.M_c*(self.ly_c**2+self.lz_c**2) # kgm^2
        self.Iyy_c  = 1/12*self.M_c*(self.lx_c**2+self.lz_c**2) # kgm^2
        self.Izz_c  = 1/12*self.M_c*(self.lx_c**2+self.ly_c**2) # kgm^2
        self.I_c = np.array([[self.Ixx_c, 0, 0],[0, self.Iyy_c, 0],[0, 0, self.Izz_c]]) # kgm^2

        # Manipulator
        self.mass_m = np.array([3, 3])      # kg
        self.len_m = np.array([1, 1])       # m
        self.wid_m = np.array([0.05, 0.05]) # m
        self.I_mi = 1/12*self.mass_m*(self.len_m**2+self.wid_m**2) # kgm^2 
        
        # Target Spacecraft
        self.M_t = 7 # kg
        self.lx_t = 0.5 # m
        self.ly_t = 0.5 # m
        self.lz_t = 0.5 # m
        self.Ixx_t  = 1/12*self.M_t*(self.ly_t**2+self.lz_t**2) # kgm^2 
        self.Iyy_t  = 1/12*self.M_t*(self.lx_t**2+self.lz_t**2) # kgm^2
        self.Izz_t  = 1/12*self.M_t*(self.lx_t**2+self.ly_t**2) # kgm^2
        self.I_t = np.array([[self.Ixx_t, 0, 0],[0, self.Iyy_t, 0],[0, 0, self.Izz_t]]) # kgm^2

    
