import textract

text = textract.process('No project is an island - Linking projects to history and context (Engwall 2003).pdf', method='pdfminer')
print(text)
