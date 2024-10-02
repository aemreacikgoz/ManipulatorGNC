# Thesis Study Main Code - Ahmet Emre Acikgoz 10896896

#### Libraries ###########################################################################
import numpy as np
import matplotlib.pyplot as plt
import scipy
from geoMassParams import Params
from defineRobot import Manipulator
from MathUtilities import matutil as mat

#### Main Code ###########################################################################
def main():
    # Geometric and Mass Parameters
    GM_Params = Params()

    # Denavit-Hartenberg Table of Manipulator
    #                    [ theta  , d, a  , alpha   ] [rad, m, m, rad]
    DH_Table = np.array([[ np.pi/6, 0, 0.5,        0],
                         [0       , 0, 1  , -np.pi/2],
                         [-np.pi/6, 0, 1  ,  np.pi/2]])

    Robot = Manipulator()
# Run the main function
if __name__ == "__main__":
    main()