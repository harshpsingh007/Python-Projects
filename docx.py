import docx2txt
path = input('Enter the file path')
text = docx2txt.process(path)
print (text)