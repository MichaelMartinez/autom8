# import tkinter to create GUI
from tkinter import *

# create a class to create GUI


class ConvertUnits:
    # create a constructor
    def __init__(self):
        # create a window
        window = Tk()
        # set the title of the window
        window.title("Convert Units")
        # create a frame
        frame = Frame(window)
        # set the frame to be packed
        frame.pack()
        # create a label that says enter a value
        Label(frame, text="Enter a value").grid(row=1, column=1, sticky=W)
        # create a label that says enter a unit
        Label(frame, text="Enter a unit").grid(row=2, column=1, sticky=W)
        # create a label that says enter a unit to convert to
        Label(frame, text="Enter a unit to convert to").grid(
            row=3, column=1, sticky=W)
        # create a label that says the converted value
        Label(frame, text="Converted value").grid(row=4, column=1, sticky=W)
        # create a variable to store the value
        self.value = StringVar()
        # create an entry box to enter the value
        Entry(frame, textvariable=self.value,
              justify=RIGHT).grid(row=1, column=2)
        # create a variable to store the unit
        self.unit = StringVar()
        # create an entry box to enter the unit
        Entry(frame, textvariable=self.unit,
              justify=RIGHT).grid(row=2, column=2)
        # create a variable to store the unit to convert to
        self.unitToConvertTo = StringVar()
        # create an entry box to enter the unit to convert to
        Entry(frame, textvariable=self.unitToConvertTo,
              justify=RIGHT).grid(row=3, column=2)
        # create a variable to store the converted value
        self.convertedValue = StringVar()
        # create a label to display the converted value
        Label(frame, textvariable=self.convertedValue).grid(
            row=4, column=2, sticky=E)
        # create a button to convert the units
        Button(frame, text="Convert", command=self.convert).grid(
            row=5, column=2, sticky=E)
        # create a button to clear the entry boxes
        Button(frame, text="Clear", command=self.clear).grid(
            row=5, column=1, sticky=W)
        # create a button to exit the program
        Button(frame, text="Exit", command=window.destroy).grid(
            row=5, column=3, sticky=E)
        # create a main loop
        window.mainloop()

    # create a method to convert the units

    def convert(self):
        # create list of units using shortend names for length, volume and mass
        units = ["m", "cm", "mm", "km", "in", "ft", "yd", "mi",
                 "L", "mL", "gal", "fl oz", "kg", "g", "lb", "oz"]
        # create list of conversion factors
        conversionFactors = [1, 0.01, 0.001, 1000, 0.0254, 0.3048, 0.9144, 1609.34,
                             0.001, 0.000001, 0.00378541, 0.0000295735, 1, 0.001, 0.453592, 0.0283495]
        # get the value from the value entry box
        value = float(self.value.get())
        # get the unit from the unit entry box
        unit = self.unit.get()
        # get the unit to convert to from the unit to convert to entry box
        unitToConvertTo = self.unitToConvertTo.get()
        # get the index of the unit in the units list
        unitIndex = units.index(unit)
        # get the index of the unit to convert to in the units list
        unitToConvertToIndex = units.index(unitToConvertTo)
        # get the conversion factor for the unit
        conversionFactor = conversionFactors[unitIndex]
        # get the conversion factor for the unit to convert to
        conversionFactorToConvertTo = conversionFactors[unitToConvertToIndex]
        # convert the value to the unit to convert to
        convertedValue = value * conversionFactor / conversionFactorToConvertTo
        # set the converted value label to the converted value
        self.convertedValue.set(convertedValue)

    # create a method to clear the entry boxes

    def clear(self):
        # clear the value entry box
        self.value.set("")
        # clear the unit entry box
        self.unit.set("")
        # clear the unit to convert to entry box
        self.unitToConvertTo.set("")
        # clear the converted value label
        self.convertedValue.set("")


# create an object of the class
ConvertUnits()
