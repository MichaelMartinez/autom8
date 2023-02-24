import os
import tkinter as tk
from tkinter import filedialog
from collections import defaultdict
import hashlib


class DuplicateFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Duplicate Finder")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.folder1_button = tk.Button(
            self, text="Select Folder 1", command=self.select_folder1)
        self.folder1_button.pack(side="top")

        self.folder1_label = tk.Label(self, text="No folder selected")
        self.folder1_label.pack(side="top")

        self.folder2_button = tk.Button(
            self, text="Select Folder 2", command=self.select_folder2)
        self.folder2_button.pack(side="top")

        self.folder2_label = tk.Label(self, text="No folder selected")
        self.folder2_label.pack(side="top")

        self.compare_button = tk.Button(
            self, text="Compare", command=self.compare_folders)
        self.compare_button.pack(side="top")

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(side="top")

    def select_folder1(self):
        folder_path = filedialog.askdirectory()
        self.folder1_label.config(text=folder_path)

    def select_folder2(self):
        folder_path = filedialog.askdirectory()
        self.folder2_label.config(text=folder_path)

    def compare_folders(self):
        folder1_path = self.folder1_label.cget("text")
        folder2_path = self.folder2_label.cget("text")

        if not folder1_path or not folder2_path:
            self.result_label.config(text="Please select both folders")
            return

        files_by_size = defaultdict(list)

        for folder_path in [folder1_path, folder2_path]:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    files_by_size[file_size].append(file_path)

        duplicate_files = []

        for size, files in files_by_size.items():
            if len(files) > 1:
                md5_by_file = defaultdict(str)
                for file_path in files:
                    with open(file_path, "rb") as f:
                        md5_by_file[file_path] = hashlib.md5(
                            f.read()).hexdigest()
                md5_by_hash = defaultdict(list)
                for file_path, md5 in md5_by_file.items():
                    md5_by_hash[md5].append(file_path)
                for md5, files in md5_by_hash.items():
                    if len(files) > 1:
                        duplicate_files.extend(files)

        if len(duplicate_files) == 0:
            self.result_label.config(text="No duplicate files found")
        else:
            self.result_label.config(
                text=f"Duplicate files:\n{', '.join(duplicate_files)}")


root = tk.Tk()
app = DuplicateFinder(master=root)
app.mainloop()
