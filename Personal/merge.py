import PyPDF2
 
path = open('recent.pdf', 'rb')
path2 = open('lastdischarge1.pdf', 'rb')
path3=open('reports1.pdf','rb')
path4=open('bills.pdf','rb')
 
merger = PyPDF2.PdfFileMerger()
 
merger.merge(position=0, fileobj=path)
merger.merge(position=1, fileobj=path2)
merger.merge(position=3, fileobj=path3)
merger.merge(position=10, fileobj=path4)

merger.write(open("test_out.pdf", 'wb'))