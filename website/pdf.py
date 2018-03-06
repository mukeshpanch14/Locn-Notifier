import time
from PyPDF2 import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from xhtml2pdf import pisa
import sys 
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 

url = 'http://www.yahoo.com'
tem_pdf = "c:\\tem_pdf.pdf"
final_file = "c:\\younameit.pdf"

app = QApplication(sys.argv)
web = QWebView()
#Read the URL given
web.load(QUrl(url))
printer = QPrinter()
#setting format
printer.setPageSize(QPrinter.A4)
printer.setOrientation(QPrinter.Landscape)
printer.setOutputFormat(QPrinter.PdfFormat)
#export file as c:\tem_pdf.pdf
printer.setOutputFileName(tem_pdf)

def convertIt():
    web.print_(printer)
    QApplication.exit()

QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

app.exec_()
sys.exit
