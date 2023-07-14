import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog, scrolledtext


class NotesViewer:
    def __init__(self, root):
        self.root = root
        self.file_listbox = None
        self.content_text = None

    def create_widgets(self):
        self._create_file_listbox()
        self._create_content_text()

    def update_file_list(self, file_list):
        self.file_listbox.delete(0, "end")
        for file_name in file_list:
            self.file_listbox.insert("end", file_name)

    def get_selected_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            return self.file_listbox.get(selected_index)
        return None

    def show_content(self, content):
        self.content_text.delete("1.0", "end")
        self.content_text.insert("1.0", content)

    def _create_file_listbox(self):
        file_frame = tk.Frame(self.root)
        file_frame.pack(side="left", fill="y")

        file_label = tk.Label(file_frame, text="Files")
        file_label.pack()

        scrollbar = tk.Scrollbar(file_frame)
        scrollbar.pack(side="right", fill="y")

        self.file_listbox = tk.Listbox(file_frame, yscrollcommand=scrollbar.set)
        self.file_listbox.pack(fill="both", expand=True)

        scrollbar.config(command=self.file_listbox.yview)

    def _create_content_text(self):
        content_frame = tk.Frame(self.root)
        content_frame.pack(side="left", fill="both", expand=True)

        content_label = tk.Label(content_frame, text="Content")
        content_label.pack()

        self.content_text = scrolledtext.ScrolledText(content_frame, wrap="word")
        self.content_text.pack(fill="both", expand=True)
