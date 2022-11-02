from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
import re

def get_pdf_file_content(path_to_pdf):
    resource_manager = PDFResourceManager(caching=True)
    out_text = StringIO()
    codec = 'utf-8'
    laParams = LAParams()
    text_converter = TextConverter(resource_manager, out_text, laparams=laParams)
    fp = open(path_to_pdf, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, text_converter)
    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)
    text = out_text.getvalue()
    fp.close()
    text_converter.close()
    out_text.close()
    text = re.sub('[^a-zA-Z0-9:/ \n\.]', '', text)
    return text

if __name__ == '__main__':
    # path_to_pdf = "D://ML Projects//pdfminer//Banned_entities.pdf"
    # path_to_pdf = "D://ML Projects//pdfminer//Russian2.pdf"
    path_to_pdf = "jjj.pdf"

    #open text file
    text_file = open("jjj.txt", "w", encoding='utf-8')
    
    a = get_pdf_file_content(path_to_pdf)
    #write string to file
    text_file.write(a)
    
    #close file
    text_file.close()

