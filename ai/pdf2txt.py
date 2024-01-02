## python pdf_to_text.py input_pdf_file.pdf output_text_file.txt


import sys
import PyPDF2


def pdf_to_text(pdf_file_path, text_file_path):
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        with open(text_file_path, "w", encoding="utf-8") as text_file:
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num].extract_text()
                text_file.write(page)

    print(f"PDF file {pdf_file_path} has been converted to text file {text_file_path}")


# Accept input and output file paths from command line arguments
if len(sys.argv) != 3:
    print("Usage: python pdf_to_text.py <input_pdf_file> <output_text_file>")
    sys.exit(1)

pdf_file_path = sys.argv[1]
text_file_path = sys.argv[2]

# Call the function to convert the PDF file to text file
pdf_to_text(pdf_file_path, text_file_path)
