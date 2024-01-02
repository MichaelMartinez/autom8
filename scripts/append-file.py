import tkinter as tk
from tkinter import filedialog
import os

# Configure logging
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Function to strip white space from file content
def strip_whitespace(content):
    return "".join(content.split())


# Function to process files and append content to the output file
def process_files(file_paths):
    try:
        # Extract file names without extensions
        file_names = [os.path.splitext(os.path.basename(f))[0] for f in file_paths]

        # Create the output file name
        output_file_name = "-".join(file_names) + ".txt"

        # Open the output file in write mode
        with open(output_file_name, "w") as output_file:
            for file_path in file_paths:
                logging.info(f"Processing {file_path}")
                with open(file_path, "r") as file:
                    output_file.write(
                        os.path.basename(file_path) + "\n"
                    )  # Write the file name
                    file_content = file.read()
                    output_file.write(
                        strip_whitespace(file_content) + "\n"
                    )  # Write the stripped content
        logging.info(f"All files have been processed and saved to {output_file_name}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def main():
    # Set up the GUI for file selection
    root = tk.Tk()
    root.withdraw()  # We don't want a full GUI, so keep the root window from appearing
    root.update()

    # Show an "Open" dialog box and return the path to the selected file(s)
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Text files", "*.txt;*.py;*.css;*.html;*.yaml")],
        title="Choose files",
    )

    # Process the files if any were selected
    if file_paths:
        process_files(file_paths)
    else:
        logging.info("No files were selected.")

    root.destroy()


if __name__ == "__main__":
    main()
