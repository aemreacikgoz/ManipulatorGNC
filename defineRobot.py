import numpy as np
import matplotlib.pyplot as plt
import scipy
from MathUtilities import matutil as mat
class Manipulator:
    def _init_(self,DH_Table):
        self.name="robot" # Robot Name (arbitrary for now)
        self.Initialize(DH_Table) # Initial configuration of the manipulator
    def Initialize(self,DH_Table):
        n_j = DH_Table.shape[0] # number of joints
        T_con = [] # consecutive rotations 
        for i in range(0,n_j):
            theta_i = DH_Table[i][0]
            d_i     = DH_Table[i][1]
            a_i     = DH_Table[i][2]
            alpha_i = DH_Table[i][3]
            T_con[i] = self.T_jmpi1_to_jmi(theta_i,alpha_i)

    def T_jmpi1_to_jmi(self,theta_i,alpha_i,a_i,d_i):
        R = self.R_jmpi1_to_jmi(theta_i,alpha_i)
        r = self.r_jmi_to_jmip1(theta_i,a_i,d_i) 
        return np.block([[R,r],[np.zeros((1,3)), 1]])
    def R_jmpi1_to_jmi(self,theta_i,alpha_i):
        return np.matmul(mat.Rot_z(theta_i).transpose() ,mat.Rot_x(alpha_i).transpose())    
    def r_jmi_to_jmip1(self,theta_i,a_i,d_i):
        return np.array([[a_i*np.cos(theta_i), a_i*np.sin(theta_i), d_i]]).transpose()    
    
    
    # Below functions shall be defined for links not joints!
    def Bij(ri, rj):
        eye = np.array([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
        c_skw = mat.skwSymm(rj-ri)
        B = np.array([[eye,np.zeros((3,3))],[c_skw, eye]])
    def p_i(R_i2I,r_ip1,r_i):
        ki = np.matmul(R_i2I,np.array([[0,0,1]]).transpose)
        c_unit = mat.vecnorm(r_ip1-r_i)
        return np.block([[ki, np.cross(ki, c_unit)]])