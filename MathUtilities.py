import numpy as np
import matplotlib.pyplot as plt
import scipy

class matutil:      
    def Rot_x(angle):
        return np.array([[1,             0,              0],
                         [0, np.cos(angle), -np.sin(angle)],
                         [0, np.sin(angle),  np.cos(angle)]])
    def Rot_y(angle):
        return np.array([[ np.cos(angle), 0, np.sin(angle)],
                         [             0, 1,             0],
                         [-np.sin(angle), 0, np.cos(angle)]])
    def Rot_z(angle):
        return np.array([[np.cos(angle), -np.sin(angle), 0],
                         [np.sin(angle),  np.cos(angle), 0],
                         [            0,              0, 1]])
    def skwSymm(vec):
        return np.array([[      0, -vec[2],  vec[1]],
                         [ vec[2],       0, -vec[0]],
                         [-vec[1],  vec[0],       0]])
    def vecnorm(vec):
        return np.sqrt(vec[0]**2+vec[1]**2+vec[2]**2)
    
