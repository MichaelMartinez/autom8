import os


def split_text_file(filepath, word_limit=500):
    with open(filepath, "r") as file:
        text = file.read()
        words = text.split()

    total_words = len(words)
    # Calculate the number of chunks needed
    num_chunks = max(1, total_words // word_limit + (total_words % word_limit > 0))

    for i in range(num_chunks):
        # Calculate the start and end indices for each chunk
        start = i * word_limit
        end = min((i + 1) * word_limit, total_words)
        chunk = " ".join(words[start:end])
        # Write each chunk to a new file
        with open(f"{filepath}_part_{i + 1}.txt", "w") as chunk_file:
            chunk_file.write(chunk)


def process_folder(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            split_text_file(filepath)


# Example use with a folder path
process_folder("D:/CODE/autom8/datasets")
