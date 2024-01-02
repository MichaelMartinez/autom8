from ebooklib import epub
import ebooklib


def epub_to_text(epub_file_path, output_text_file):
    book = epub.read_epub(epub_file_path)
    text_content = []

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            text_content.append(item.get_body_content().decode("utf-8"))

    with open(output_text_file, "w", encoding="utf-8") as file:
        file.write("\n".join(text_content))


# Usage
# epub_file_path = 'path_to_your_epub_file.epub'
# output_text_file = 'output_text.txt'
# epub_to_text(epub_file_path, output_text_file)
