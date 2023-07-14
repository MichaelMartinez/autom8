import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog, scrolledtext
from notes_manipulator import NotesManipulator


def main():
    root = tk.Tk()
    notes_manipulator = NotesManipulator(root)
    notes_manipulator.run()
    root.mainloop()


if __name__ == "__main__":
    main()
