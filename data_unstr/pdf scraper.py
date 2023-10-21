import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf_document:
        num_pages = pdf_document.page_count
        for page_num in range(num_pages):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
    return text

def write_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

pdf_path = "4.pdf"  # Replace with your PDF file path
output_file = "4.txt"  # Replace with the desired output file name

extracted_text = extract_text_from_pdf(pdf_path)
write_text_to_file(extracted_text, output_file)


with open('4.txt' , 'r') as file:

