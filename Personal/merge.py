# importing required modules
import PyPDF2
 
def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()
 
    # appending pdfs one by one
    for pdf in pdfs:
        with open(pdf, 'rb') as f:
            pdfMerger.append(f)
 
    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)
 
def main():
    # pdf files to merge
    pdfs = ['recent.pdf','lastdischarge1.pdf', 'reports1.pdf','bills.pdf']
 
    # output pdf file name
    output  = '1296311_mediclaim.pdf'
 
    # calling pdf merge function
    PDFmerge(pdfs = pdfs, output = output)
 
if __name__ == "__main__":
    # calling the main function
    main()