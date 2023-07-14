class NotesSearcher:
    def search_notes(self, file_list, search_term):
        search_results = []
        for file_name in file_list:
            if search_term.lower() in file_name.lower():
                search_results.append(file_name)
        return search_results
