import os
from PyPDF2 import PdfReader, PdfWriter

# Open the input PDF file
input_pdf = PdfReader(open('Martinez1203.pdf', 'rb'))

# Get the total number of pages in the input PDF file
total_pages = len(input_pdf.pages)

# Split the input PDF file into separate 5-page PDFs
for i in range(0, total_pages, 5):
    # Create a new PDF file for the current set of 5 pages
    output_pdf = PdfWriter()

    # Add the current set of 5 pages to the new PDF file
    for j in range(i, min(i+5, total_pages)):
        output_pdf.add_page(input_pdf.pages[j])

    # Save the new PDF file with a unique name
    output_filename = 'Martinez_1203_{}.pdf'.format(i//5+1)
    with open(output_filename, 'wb') as f:
        output_pdf.write(f)

    # Print a message to indicate progress
    print('Created {} with pages {}-{}'.format(output_filename,
          i+1, min(i+5, total_pages)))
