#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import csv
import io

def convert_pdf_to_txt(path):
    # reading pdf converting into txt file
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

    with open(path, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        caching = True
        pagenos = set()
        count  = 0
        for page in PDFPage.get_pages(fp, pagenos, password=password,caching=caching, check_extractable=True):
            if(count >=3 and count <=35):
                interpreter.process_page(page)
            count+=1

        text = retstr.getvalue()

    device.close()
    retstr.close()
    return text

f = open('output.txt','w')
print >>f, convert_pdf_to_txt("001-001.pdf")

filne = "output.txt"
list_final = []

print("csv saved")

with open(filne,'r+') as f:
    i = 0 
    for line in f:
        # print(line)
        if line.startswith("નામ : ગઢવી લાલદાન"):
            list_temp = {}
            # print f.next() 
            list_temp[0] = line
            list_temp[1] = f.next()
            list_temp[2] = f.next()
            list_temp[3] = f.next()
            j = 0
            list_final.append(list_temp) 
            i+=1

