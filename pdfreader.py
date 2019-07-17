import PyPDF2
pdfFileObj = open('No project is an island - Linking projects to history and context (Engwall 2003).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
print(text)
