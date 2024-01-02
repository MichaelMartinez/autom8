# This Code is for testing the python output of the llama model with a lora

# error here
#import tkinter

from tkinter import *


class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        # Initialize the window
        self.title("Weight Converter")
        self.geometry('600x350')

        # Create the text boxes
        self.pounds = tkinter.Label(
            text="Pounds:", fg='black', bg='white').pack()
        self.grams = tkinter.Label(
            text="Grams:", fg='black', bg='white').pack()

        # Create the buttons
        self.calculate_button = tkinter.Button(
            text="Calculate", command=self.calculate).pack()
        self.reset_button = tkinter.Button(
            text="Reset", command=self.reset).pack()

        # Create the entry field
        self.entry_field = tkinter.Entry().pack()

    def reset(self):
        # Reset the values of the fields
        self.entry_field.delete(0, 'end')
        self.pounds['text'] = ''
        self.grams['text'] = ''
        self.calculate_button['command'] = None

    def calculate(self):
        # Get the value from the entry field
        pound_value = float(self.entry_field.get())
        gram_value = (pound_value / 2.2)
        # Set the values for the labels
        self.pounds['text'] = str(pound_value) + 'lbs'
        self.grams['text'] = str(gram_value) + 'grms'


App()
