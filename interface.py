import ctypes
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

mylib = ctypes.CDLL('C:\\Users\\mat3u\\OneDrive\\Dokumenty\\GitHub\\basic-control-system-repo\\sharedLib.so')

# Define argument and return types
mylib.output.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
mylib.output.restype = ctypes.POINTER(ctypes.c_double)

def call_output_function(dStop, dTs, dU):
    result_ptr = mylib.output(dStop, dTs, dU)
    result_list = [result_ptr[i] for i in range(100)]  # Assuming the loop runs 100 times
    mylib.free(result_ptr)  # Free memory allocated by the C++ function
    return result_list

dStop = 1.0
dTs = 0.1
dU = 0.5
#output_list = call_output_function(dStop, dTs, dU)
#print(output_list)

# FUNCTIONS
def plot_data():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Create a Figure and add a subplot
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(1, 1, 1)

    # Plot the data
    ax.plot(x, y, marker='o')

    # Add labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Data Plot')

    # Display the plot on the Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# MAIN

# Create the main window
root = tk.Tk()
root.title('Data Plotter')

# Create a frame for the plot
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a Plot button
plot_button = ttk.Button(root, text='Plot Data', command=plot_data)
plot_button.pack()

# Start the main loop
root.mainloop()
