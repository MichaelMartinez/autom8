import chardet
import tkinter as tk
from tkinter import filedialog
import os
import re
from collections import Counter
import markdown


def save_results(results, total_word_count, word_frequency):
    # Prompt the user to choose a location to save the results
    save_path = filedialog.asksaveasfilename(
        defaultextension=".md",
        filetypes=(("Markdown files", "*.md"), ("All files", "*.*")),
    )

    if save_path:
        with open(save_path, "w", encoding="utf-8") as file:
            file.write("# Analysis Results\n\n")
            file.write(f"Total Word Count: {total_word_count}\n\n")

            file.write("File Details:\n\n")
            for result in results:
                filename = result["filename"]
                word_count = result["word_count"]
                word_frequency = result["word_frequency"]
                less_than_10_words = result["less_than_10_words"]
                date = result["date"]

                file.write(
                    f"## {'**' + filename + '**' if less_than_10_words else filename}\n"
                )
                file.write("\n")
                file.write(f"- Word Count: {word_count}\n")
                for word, count in word_frequency.most_common(10):
                    file.write(f"    - {word}: {count}\n")
                file.write("\n")
                if less_than_10_words:
                    file.write("\n")
                    file.write("**LESS THAN 10 WORDS**\n")
                if date:
                    file.write(f"\nDate: {date}\n")
                file.write("\n")

                # Write the top 10 most frequent words
                file.write("Top 10 Most Frequent Words:\n\n")
                for word, count in word_frequency.most_common(10):
                    file.write(f"- {word}: {count}\n")
                file.write("\n")

        print("Results saved successfully.")


def get_word_count(filepath, encoding="utf-8"):
    # Define the set of ignored words (conjunctions)
    ignored_words = {
        "and",
        "but",
        "or",
        "nor",
        "for",
        "yet",
        "so",
    }
    # Open file, detect encoding, and count the number of words
    with open(filepath, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)

        encoding = result["encoding"]
        confidence = result["confidence"]

        if encoding and confidence > 0.5:
            try:
                content = raw_data.decode(encoding, errors="replace")
                content = re.sub(r"http\S+|www\S+", "", content)

                # Remove numbers with colons
                content = re.sub(r"\b\d+:\b", " ", content)

                # Remove special characters
                content = re.sub(r"[^\w\s]", " ", content)

                # Extract unique words
                words = re.findall(r"\b\w+\b", content.lower())
                # filtered_words = [word for word in words if word not in ignored_words]
                filtered_words = list(
                    filter(lambda word: word not in ignored_words, words)
                )
                print(f"Found {len(filtered_words)} words in {filepath}")
                return len(filtered_words)
            except UnicodeDecodeError:
                print(
                    f"Unable to decode {filepath} with detected encoding. Skipping the file."
                )
        else:
            print(f"Unable to detect encoding for {filepath}. Skipping the file.")

    return 0  # Return 0 in case of decoding failure


def count_words_in_markdown(filepath, ignored_words):
    # Detect encoding and read raw data
    with open(filepath, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)

    encoding = result["encoding"]
    confidence = result["confidence"]

    if encoding and confidence > 0.5:
        try:
            # Decode the content with detected encoding
            with open(filepath, "r", encoding=encoding, errors="replace") as file:
                content = file.read()
                html_content = markdown.markdown(content)

                # Remove HTML tags
                html_content = re.sub("<.*?>", "", html_content)

                # Remove numbers and URLs
                html_content = re.sub(r"\b\d+:\b|\b\d+\b", " ", html_content)
                html_content = re.sub(
                    r"<(https:\/\/|http:\/\/|www)\S+(?=\s|$)", "", html_content
                )

                # Remove special characters
                html_content = re.sub(r"[^\w\s]", " ", html_content)

                # Extract unique words
                words = re.findall(r"\b\w+\b", html_content.lower())
                filtered_words = list(
                    filter(lambda word: word not in ignored_words, words)
                )
                print(f"Found {len(filtered_words)} words in {filepath}")
                return len(filtered_words)
        except UnicodeDecodeError:
            print(
                f"Unable to decode {filepath} with detected encoding. Skipping the file."
            )
    else:
        print(f"Unable to detect encoding for {filepath}. Skipping the file.")

    return 0  # Return 0 in case of decoding failure


def analyze_folder():
    # Prompt the user to select a folder
    folder_path = filedialog.askdirectory()

    if folder_path:
        word_count = 0
        word_frequency = Counter()
        results = []

        # Walk through the directory and analyze markdown files
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    file_word_count = count_words_in_markdown(file_path, ignored_words)
                    # file_word_count = get_word_count(file_path)
                    word_count += file_word_count

                    # Read file content and count word frequency
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        words = re.findall(r"\w+", content)
                        word_frequency.update(words)

                    # Find if the file has less than 10 words
                    less_than_10_words = file_word_count < 10

                    # Find the date in the file, if available
                    # date = re.findall(r"\d{2}-\d{2}-\d{4}", content)
                    # Find the date in the file, if available
                    pattern = r"\b((?:0?[1-9]|1[0-2])-(?:0?[1-9]|[12]\d|3[01])-(?:\d{4}|\d{2})|(?:\d{4}|\d{2})-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[12]\d|3[01]))\b"
                    date_matches = re.findall(pattern, content)
                    date = date_matches[0] if date_matches else None

                    # Store file details in the results list
                    result = {
                        "filename": file,
                        "word_count": file_word_count,
                        "word_frequency": Counter(words),
                        "less_than_10_words": less_than_10_words,
                        "date": date[0] if date else None,
                    }
                    results.append(result)

        # Save results to a markdown file
        save_results(results, word_count, word_frequency)


# Create the main window
root = tk.Tk()

# Create a file dialog button
file_dialog_button = tk.Button(root, text="Choose Folder", command=analyze_folder)
file_dialog_button.pack()

# Run the main loop
root.mainloop()
