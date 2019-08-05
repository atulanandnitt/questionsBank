def readCsv():

    with open("csvfile.csv","r") as f1:
        data = f1.read()
        print(data)

#readCsv()


import docx2txt

def readDoc():

    # extract text
    text = docx2txt.process("basic_practice_notes.docx")
    print(text)
    # extract text and write images in /tmp/img_dir
    text = docx2txt.process("basic_practice_notes.docx", "/tmp/img_dir")

readDoc()


import PyPDF2

def readPdf():

    pdfFileObj = open('0801-Paper.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader)
    print(pdfReader.numPages)
    for i in range(pdfReader.numPages):

        pageObj = pdfReader.getPage(i)
        print(pageObj.extractText())


readPdf()

print("extra methods************need additional packages to be installed***********************")

"""
import Document



def readDoc():


    document = Document()
    document.save('test.docx')
    with open("basic_practice_notes.docx", "r") as f1:
        data = f1.read()
        print(data)

#from docx import Document

def readDoc1():

    document = Document('basic_practice_notes.docx')
    for para in document.paragraphs:
        print(para.text)


#readDoc1()
"""