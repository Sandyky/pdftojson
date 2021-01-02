# pypdf_text_generator.py

# importing required modules 
import PyPDF2 

def extract_text_by_page(pdf_path):

    # creating a pdf file object 
    
    pdfFileObj = open(pdf_path, 'rb') # pdfFileObj = open('Test for json (2) (1).pdf', 'rb')


    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    # printing number of pages in pdf file 
    print(pdfReader.numPages) 

    # creating a page object 
    for pageNumber in range(0,pdfReader.numPages):
        
        pageObj = pdfReader.getPage(pageNumber)
        # extracting text from page 
        text = pageObj.extractText()
        yield text

    # closing the pdf file object 
    pdfFileObj.close() 

