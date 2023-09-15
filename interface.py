import tkinter as tk
import control
import numpy as np
import matplotlib.pyplot as plt 

# Defining model 
def LinearObj(num, den):
    H = control.tf(num, den)
    print(H)
    return H    

# Defining plot function
def Plot(H):
    t,y = control.step_response(H)
    plt.plot(t,y)
    plt.title("Step Response")
    plt.grid()
    plt.show()

# Defining Str to List
def stringToList(str):
    integer_list = []  # Create an empty list to store the integers
    
    # Split the input string by commas and iterate over the parts
    parts = str.split(',')
    for part in parts:
        try:
            integer = int(part)  # Convert each part to an integer
            integer_list.append(integer)  # Append the integer to the list
        except ValueError:
            pass  # Ignore non-integer parts
    
    return integer_list  

# Defining graph
def graph(entryNum,entryDen):
    num = stringToList(entryNum.get())
    den = stringToList(entryDen.get())
    H = LinearObj(num,den)
    Plot(H)

# Defining main function
def main():
    window = tk.Tk()
    window.title("Control system interface")
    window.geometry("400x200")

    labelNum = tk.Label(text="Numerator")
    labelNum.pack()

    entryNum = tk.Entry()
    entryNum.pack()
 
    labelDen = tk.Label(text="Denumerator")
    labelDen.pack()

    entryDen = tk.Entry()
    entryDen.pack() 

    buttonGen = tk.Button(window, text="Step", command=lambda:graph(entryNum,entryDen))
    buttonGen.pack()
    window.mainloop()



# Main loop
if __name__=="__main__":
    main()