import tkinter as tk
import control
import numpy as np
import matplotlib.pyplot as plt 

# Defining model 
def LinearObj(num, den):
    H = control.tf(num, den)
    return H    

# Defining plot function
def Plot(H):
    t,y = control.step_response(H)
    plt.plot(t,y)
    plt.title("Step Response")
    plt.grid()
    plt.waitforbuttonpress()

# Defining main function
def main():
    H = LinearObj([1],[2,1])
    Plot(H)

# Main loop
if __name__=="__main__":
    main()