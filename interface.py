#import ctypes
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#mylib = ctypes.CDLL('C:\\Users\\mat3u\\OneDrive\\Dokumenty\\GitHub\\basic-control-system-repo\\build\\Debug\\ControlSys.dll')
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
