# Author: Michael Martinez
# Date: 02/24/2023
import os
import tkinter as tk
from tkinter import messagebox
# import the file dialog module
import tkinter.filedialog as filedialog

# function to find duplicates in two directories
def find_duplicates(dir1, dir2):
    duplicates = set()
    dir1_files = set(os.listdir(dir1))
    for filename in os.listdir(dir2):
        if filename in dir1_files:
            duplicates.add(filename)
    return duplicates

# function to display duplicates in the GUI
def display_duplicates():
    dir1 = dir1_entry.get()
    dir2 = dir2_entry.get()
    duplicates = find_duplicates(dir1, dir2)
    if duplicates:
        duplicates_listbox.delete(0, tk.END)
        for filename in duplicates:
            duplicates_listbox.insert(tk.END, filename)
    else:
        messagebox.showinfo("No duplicates found")

# create the tkinter window
window = tk.Tk()
window.title("Duplicate Finder")
window.geometry("1000x1000")

# create the directory input widgets
dir1_label = tk.Label(window, text="Directory 1:")
dir1_label.pack()
dir1_entry = tk.Entry(window)
dir1_entry.pack()

# create the "Select Directory 1" button
dir1_button = tk.Button(window, text="Select Directory 1", command=lambda: dir1_entry.insert(0, filedialog.askdirectory()))
dir1_button.pack()

dir2_label = tk.Label(window, text="Directory 2:")
dir2_label.pack()
dir2_entry = tk.Entry(window)
dir2_entry.pack()

# create the "Select Directory 2" button
dir2_button = tk.Button(window, text="Select Directory 2", command=lambda: dir2_entry.insert(0, filedialog.askdirectory()))
dir2_button.pack()

# create the button to find duplicates
find_button = tk.Button(window, text="Find Duplicates", command=display_duplicates)
find_button.pack()

# create the listbox to display duplicates
duplicates_listbox = tk.Listbox(window)
duplicates_listbox.pack(fill=tk.BOTH, expand=True)

# make the listbox scrollable
scrollbar = tk.Scrollbar(duplicates_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
duplicates_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=duplicates_listbox.yview)

# start the tkinter event loop
window.mainloop()
