import tkinter as tk
from tkinter import messagebox
import control
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
def graph(entryNum,entryDen,ax,canvas):
    ax.clear() 
    ax.grid()
    num = stringToList(entryNum.get())
    den = stringToList(entryDen.get())
    H = LinearObj(num,den)
    t,y = control.step_response(H)
    ax.plot(t,y)
    canvas.draw()
    #Plot(H)

# Defining main function (GUI)
def main():
    # Initialize Tkinter
    window = tk.Tk()
    window.title("Control system interface")
    window.geometry("800x800")
    frame = tk.Frame(window)
    frame.pack()
    bottomframe = tk.Frame(window)
    bottomframe.pack( )
    bottomframeGraph = tk.Frame(window)
    bottomframeGraph.pack()
    bottomframeButtons = tk.Frame(window)
    bottomframeButtons.pack()
    ipadding = {'ipadx': 10, 'ipady': 10, 'padx': 10}



    labelNum = tk.Label(frame, text="Numerator:",font=('Arial 24'))
    labelNum.pack(ipadding,side = tk.LEFT,padx = 10)

    entryNum = tk.Entry(frame, font=('Arial 24'))
    entryNum.pack(side = tk.LEFT)

    labelDen = tk.Label(bottomframe, text="Denumerator:", font=('Arial 24'))
    labelDen.pack(ipadding,side = tk.LEFT,padx = 10)

    entryDen = tk.Entry(bottomframe, font=('Arial 24'))
    entryDen.pack(side = tk.LEFT) 

    # Embedding plot
    fig,ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig,master = bottomframeGraph)
    canvas.get_tk_widget().pack(pady=10)
    buttonGen = tk.Button(bottomframeButtons, text="Step", command=lambda:graph(entryNum,entryDen,ax,canvas),font=('Arial 24'))
    buttonGen.pack(**ipadding, expand=True, fill=tk.X, side=tk.LEFT)

    # defining a custom function
    def quit_tk():
        # 1) destroys all widgets and closes the main loop
        window.destroy()
        # 2) ends the execution of the Python program
        exit()

    #  Close tkinter window when the button is clicked
    buttonExit = tk.Button(bottomframeButtons, text="Close Window",command=lambda:quit_tk(),font=('Arial 24'))  
    buttonExit.pack(**ipadding, expand=True, fill=tk.X, side=tk.LEFT)
    
    window.protocol("WM_DELETE_WINDOW", quit_tk)
    window.mainloop()


# Main loop
if __name__=="__main__":
    main()
    
