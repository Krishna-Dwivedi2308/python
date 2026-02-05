# we are going to use PyMuPDF to read PDF files
import fitz


def read_pdf(file_path):
    doc = fitz.open(file_path)
    all_text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        print(text)
        all_text += text
    # print(all_text)
    doc.close()

    return


read_pdf("Full_Stack_Resume_Krishna.pdf")
