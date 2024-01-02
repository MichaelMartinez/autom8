from PyPDF2 import PdfReader, PdfWriter
import re


def remove_cpp_code_from_text(text):
    pattern = r"#include.*?#endif // XI_WIN"
    cleaned_text = re.sub(pattern, "", text, flags=re.DOTALL)
    return cleaned_text


def manipulate_text(input_txt_path, output_txt_path):
    with open(input_txt_path, "r") as file:
        text = file.read()
        manipulated_text = text.replace("Description", "--Description--")

    with open(output_txt_path, "w") as file:
        file.write(manipulated_text)


def main():
    input_pdf_path = "C:/Users/monk/Downloads/API_Samples.pdf"
    output_txt_path = "API_samples_output.txt"

    # Read the PDF and extract text
    with open(input_pdf_path, "rb") as file:
        pdf_reader = PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()

    # Remove C++ code examples
    cleaned_text = remove_cpp_code_from_text(text)
    pattern = r"((?:Copy Code.*?){1})(Copy Code)"
    fixed_text = re.sub(pattern, r"\1--", cleaned_text, flags=re.DOTALL)

    # Save the cleaned text to a plain text file
    with open(output_txt_path, "w") as file:
        file.write(fixed_text)


if __name__ == "__main__":
    main()
