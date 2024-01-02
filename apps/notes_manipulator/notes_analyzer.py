import os
import csv
from collections import Counter


class NotesAnalyzer:
    def __init__(self):
        self.folder_path = ""
        self.file_list = []
        self.file_contents = {}
        self.analyzed_data = {}

    def load_folder(self, folder_path):
        self.folder_path = folder_path
        self.file_list = self._get_file_list(folder_path)

    def analyze_notes(self):
        self.file_contents = self._read_file_contents()
        self.analyzed_data = self._analyze_data()

    def get_file_list(self):
        return self.file_list

    def get_file_content(self, file_name):
        return self.file_contents.get(file_name, "")

    def filter_files(self, filter_term):
        filtered_files = []
        for file_name in self.file_list:
            if filter_term.lower() in file_name.lower():
                filtered_files.append(file_name)
        return filtered_files

    def sort_files(self, sort_option):
        if sort_option == "name":
            return sorted(self.file_list)
        elif sort_option == "content":
            return sorted(
                self.file_list, key=lambda x: len(self.file_contents.get(x, ""))
            )
        elif sort_option == "frequency":
            return sorted(
                self.file_list,
                key=lambda x: self.analyzed_data.get(x, {}).get("frequency", 0),
                reverse=True,
            )
        else:
            return self.file_list

    def export_to_csv(self, file_path):
        headers = ["File Name", "Content Length", "Most Frequent Words"]
        rows = []
        for file_name in self.file_list:
            content_length = len(self.file_contents.get(file_name, "").split())
            most_frequent_words = ", ".join(
                self.analyzed_data.get(file_name, {}).get("most_frequent_words", [])
            )
            rows.append([file_name, content_length, most_frequent_words])

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)

    def _get_file_list(self, folder_path):
        file_list = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".md"):
                file_list.append(file_name)
        return file_list

    def _read_file_contents(self):
        file_contents = {}
        for file_name in self.file_list:
            file_path = os.path.join(self.folder_path, file_name)
            with open(file_path, "r") as file:
                file_contents[file_name] = file.read()
        return file_contents

    def _analyze_data(self):
        analyzed_data = {}
        for file_name, content in self.file_contents.items():
            content_length = len(content.split())
            most_frequent_words = self._get_most_frequent_words(content)
            analyzed_data[file_name] = {
                "content_length": content_length,
                "most_frequent_words": most_frequent_words,
            }
        return analyzed_data

    def _get_most_frequent_words(self, content):
        words = content.lower().split()
        word_counts = Counter(words)
        most_common_words = word_counts.most_common(5)
        return [word for word, count in most_common_words]
