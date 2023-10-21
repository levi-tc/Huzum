import fitz  # PyMuPDF


def read_pdf(pdf_path):
    doc = fitz.open(pdf_path)

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = page.get_text()
        print(f"Page {page_num + 1}:\n{text}\n")

    doc.close()

pdf_path = "data_unstr/1.pdf"  # Replace with your PDF file path
read_pdf(pdf_path)

