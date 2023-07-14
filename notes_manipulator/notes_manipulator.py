import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog, scrolledtext
from notes_analyzer import NotesAnalyzer
from notes_viewer import NotesViewer
from notes_searcher import NotesSearcher


class NotesManipulator:
    def __init__(self, root):
        self.root = root
        self.notes_analyzer = NotesAnalyzer()
        self.notes_viewer = NotesViewer(root)
        self.notes_searcher = NotesSearcher()

    def run(self):
        self._create_widgets()

    def _create_widgets(self):
        self._create_menu()
        self.notes_viewer.create_widgets()

    def _create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open Folder", command=self._open_folder)
        file_menu.add_command(label="Analyze", command=self._analyze)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="View Content", command=self._view_content)
        view_menu.add_command(label="Search", command=self._search)
        view_menu.add_separator()
        view_menu.add_command(label="Filter Files", command=self._filter_files)
        view_menu.add_command(label="Sort Files", command=self._sort_files)
        menu_bar.add_cascade(label="View", menu=view_menu)

        export_menu = tk.Menu(menu_bar, tearoff=0)
        export_menu.add_command(label="Export to CSV", command=self._export_to_csv)
        menu_bar.add_cascade(label="Export", menu=export_menu)

    def _open_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.notes_analyzer.load_folder(folder_path)
            self.notes_viewer.update_file_list(self.notes_analyzer.get_file_list())

    def _analyze(self):
        self.notes_analyzer.analyze_notes()
        self.notes_viewer.update_file_list(self.notes_analyzer.get_file_list())

    def _view_content(self):
        selected_file = self.notes_viewer.get_selected_file()
        if selected_file:
            content = self.notes_analyzer.get_file_content(selected_file)
            self.notes_viewer.show_content(content)

    def _search(self):
        search_term = simpledialog.askstring("Search", "Enter search term:")
        if search_term:
            search_results = self.notes_searcher.search_notes(
                self.notes_analyzer.get_file_list(), search_term
            )
            self.notes_viewer.update_file_list(search_results)

    def _filter_files(self):
        filter_term = simpledialog.askstring("Filter", "Enter filter term:")
        if filter_term:
            filtered_files = self.notes_analyzer.filter_files(filter_term)
            self.notes_viewer.update_file_list(filtered_files)

    def _sort_files(self):
        sort_option = simpledialog.askstring(
            "Sort", "Enter sort option (name/content/frequency):"
        )
        if sort_option:
            sorted_files = self.notes_analyzer.sort_files(sort_option)
            self.notes_viewer.update_file_list(sorted_files)

    def _export_to_csv(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )
        if file_path:
            try:
                self.notes_analyzer.export_to_csv(file_path)
                messagebox.showinfo("Export", "Data exported successfully!")
            except Exception as e:
                messagebox.showerror("Export", f"Error exporting data: {str(e)}")
