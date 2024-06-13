from tkinter import *


def miles_to_km():
    miles_value = int(input.get())
    convert = round(miles_value * 1.609344)
    result.config(text=convert)


# Creating a new window and configurations
window = Tk()
window.title("Miles to km Converter")
window.minsize(width=100, height=100)
window.config(padx=100, pady=100)

# Labels
label = Label(text="is equal to", font=("Arial", 16))
label.config(padx=20, pady=20)
label.grid(column=0, row=1)
miles = Label(text="Miles", font=("Arial", 16))
miles.config(padx=20, pady=20)
miles.grid(column=2, row=0)
result = Label(text="0", font=("Arial", 16))
result.config(padx=20, pady=20)
result.grid(column=1, row=1)
km = Label(text="Km", font=("Arial", 16))
km.config(padx=20, pady=20)
km.grid(column=2, row=1)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.config(padx=20, pady=20)
button.grid(column=1, row=2)

window.mainloop()
