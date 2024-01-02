import chardet
import tkinter as tk
from tkinter import filedialog
import os
import re
from collections import Counter
from ignored_words import ignored_words


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

            file.write("Top 20 Most Frequent Words:\n\n")
            for word, count in word_frequency.most_common(20):
                file.write(f"- {word}: {count}\n")
            file.write("\n\n")

            file.write("File Details:\n\n")
            for result in results:
                filename = result["filename"]
                word_count = result["word_count"]
                less_than_10_words = result["less_than_10_words"]
                word_frequency_file = result["word_frequency"]

                file.write(
                    f"## {'**' + filename + '**' if less_than_10_words else filename}\n"
                )
                file.write(f"- Word Count: {word_count}\n")
                file.write("Top 5 Most Frequent Words:\n")
                for word, count in word_frequency_file.most_common(5):
                    file.write(f"  - {word}: {count}\n")
                file.write("\n")

        print("Results saved successfully.")


def analyze_folder():
    # Prompt the user to select a folder
    folder_path = filedialog.askdirectory()

    if folder_path:
        total_word_count = 0
        word_frequency = Counter()
        results = []

        # Walk through the directory and analyze each file
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)

                    # Detect encoding of the file
                    with open(file_path, "rb") as f:
                        raw_data = f.read()
                        result = chardet.detect(raw_data)

                    encoding = result["encoding"]

                    if encoding:
                        try:
                            # Read file content with detected encoding
                            with open(
                                file_path, "r", encoding=encoding, errors="replace"
                            ) as f:
                                content = f.read()

                                # Remove URLs and numbers
                                content = re.sub(
                                    r"<(https:\/\/|http:\/\/|www)\S+(?=\s|$)",
                                    "",
                                    content,
                                )
                                content = re.sub(r"\b\d+:\b|\b\d+\b", "", content)

                                # Remove special characters and convert to lowercase
                                content = re.sub(r"[^\w\s]", "", content).lower()

                                # Extract unique words
                                words = re.findall(r"\b\w+\b", content)

                                # Ignore common words
                                # ignored_words = {"the", "and"}
                                filtered_words = [
                                    word
                                    for word in words
                                    if word.lower() not in ignored_words
                                    and len(word) > 2
                                ]

                                # Update word frequency
                                word_frequency.update(filtered_words)

                                # Count the total words in the file
                                file_word_count = len(filtered_words)
                                total_word_count += file_word_count

                                # Find if the file has less than 10 words
                                less_than_10_words = file_word_count < 10

                                # Create word frequency counter for file
                                word_frequency_file = Counter(filtered_words)

                                # Store file details in the results list
                                result = {
                                    "filename": file,
                                    "word_count": file_word_count,
                                    "less_than_10_words": less_than_10_words,
                                    "word_frequency": word_frequency_file,
                                }
                                results.append(result)

                        except UnicodeDecodeError:
                            print(
                                f"Unable to decode {file_path} with detected encoding. Skipping the file."
                            )

                    else:
                        print(
                            f"Unable to detect encoding for {file_path}. Skipping the file."
                        )

        # Save results to a markdown file
        save_results(results, total_word_count, word_frequency)


# Create the main window
root = tk.Tk()

# Create a file dialog button
file_dialog_button = tk.Button(root, text="Choose Folder", command=analyze_folder)
file_dialog_button.pack()

# Run the main loop
root.mainloop()
