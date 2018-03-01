from PyPDF2 import PdfFileReader, PdfFileWriter

with open("newpdf.pdf",'rb') as infile:
    reader=PdfFileReader(infile)
    writer=PdfFileWriter()
    writer.addPage(reader.getPage(0))


outputStream = open("PyPDF2-output.pdf", "wb")
writer.write(outputStream)