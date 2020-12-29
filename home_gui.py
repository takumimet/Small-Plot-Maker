import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, 
    NavigationToolbar2Tk
)

from string_process import (
    NotANumber,
    string_to_int,
    string_to_list,
    has_decimals
)

plt.style.use("seaborn")

""" ROOT CHARACTERISTICS """
root = tk.Tk()
root.title("Plot Maker")
root.geometry("1025x450")


""" MATPLOTLIB FIGURE """

mat_fig = Figure(figsize=(6, 4), dpi=100)

mat_canvas = FigureCanvasTkAgg(mat_fig, master=root)
mat_canvas.draw()
mat_canvas.get_tk_widget().grid(row=0, 
                                column=0,
                                padx=15,
                                pady=20)


""" OPTIONS FRAME """

options_frame = tk.Frame(root)
options_frame.grid(row=0,
                   column=1,
                   padx=15,
                   pady=10)


""" OPTIONS FRAME TEXT LABELS """

    # Text of the dropdown menu
text_dropdown = tk.Label(options_frame,
                         text='Plot type:',
                         padx=10)
text_dropdown.grid(row=0, 
                   column=0,
                   pady=15)

    # Text of x
text_x = tk.Label(options_frame,
                  text='X input:',
                  padx=10)
text_x.grid(row=1, 
            column=0,
            pady=15)

    # Text of y
text_y = tk.Label(options_frame,
                  text='Y input:',
                  padx=10)
text_y.grid(row=2, 
            column=0,
            pady=15)



""" VARIABLES """

options_click = tk.StringVar()
options_click.set("Bar")

x_variables = tk.StringVar()
x_variables.set("1, 2, 3, 4, 5, 6, 7, 8, 9")

y_variables = tk.StringVar()
y_variables.set("1, 4, 9, 16, 25, 36, 49, 64, 81")


""" COMMANDS """

def extract_entries():
    """ Extract the varibles from the Entries
        and transform them into what we need """
    output_X = string_to_list(x_variables.get())
    output_Y = string_to_int(y_variables.get())

    return output_X, output_Y



def create_plot():
    """ First extracts the data from Entries
        adds new plot into Figure instance
        and then plot the data in root window """

    # TODO Ensure only x_ticks are shown
    # because if you change something 
    # right now it doesn't raise an error

    X, Y = extract_entries()    
    option = options_click.get()
    mat_fig.clear()

    # Adds the new plot unto the Figure instance
    graph_plot = mat_fig.add_subplot(111)
    # Plots the data
    if option == "Bar":
        graph_plot.bar(X, Y,
                   tick_label=X)
    elif option == "Line":
        graph_plot.plot(X, Y)
    
    elif option == "Pie":
        graph_plot.pie(Y, labels=X)

    # Displays the plot
    mat_canvas.draw()

 
""" ENTRIES """

entry_x = tk.Entry(options_frame,
                   textvariable=x_variables,
                   width=40)
entry_x.grid(row=1, column=1)


entry_y = tk.Entry(options_frame,
                   textvariable=y_variables,
                   width=40)
entry_y.grid(row=2, column=1)



""" BUTTONS """

    # Options for dropdown menu
options = [
    "Bar",
    "Line",
    "Pie"
]
    # Dropdown menu
options_dropdown = tk.OptionMenu(options_frame, options_click, *options)
options_dropdown.grid(row=0, 
                      column=1,
                      padx=5,
                      pady=15,
                      ipadx=60)

    # Create plot button
plot_button = tk.Button(options_frame,
                        text="Create plot!",
                        command=create_plot)
plot_button.grid(row=3, 
                 column=1,
                 padx=5,
                 pady=15,
                 ipadx=60)


""" MAIN LOOP """
tk.mainloop()