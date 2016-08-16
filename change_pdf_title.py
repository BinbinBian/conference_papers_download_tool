# change pdf title
#import PyPDF2 as pyPdf
from __future__ import print_function
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import shutil
import time
start = time.time()
if len(sys.argv)<2:
    print("usage: python xxx.py dir_of_pdf_files")
pdf_dir = sys.argv[1]
import os

def get_pdf_title(pdf_file_path):
    # must be open as 'rb', otherwise will raise "PdfReadError: EOF marker not found"
    with open(pdf_file_path,'rb') as f:
        pdf_reader = PdfFileReader(f) 
        # print(pdf_file_path)
        # print(pdf_reader.getDocumentInfo())
        if '/Title' in pdf_reader.getDocumentInfo().keys():
            return pdf_reader.getDocumentInfo()['/Title']
        else:
            return None

filenames = os.listdir(pdf_dir)
illegal_chars = ['\\','/',':','*','?','"','<','>','|']
# to change cvpr paper names to "16 cvpr <title>"
for fn in filenames:
    if '.pdf' in fn:
        if not "16 cvpr" in fn:
            title = get_pdf_title(pdf_dir+'/'+fn)
            if title is None:
                continue
            # res_name = "16 cvpr "+title+'.pdf'
            for c in illegal_chars:
                title = title.replace(c,"")
            res_name = "16 cvpr "+title+'.pdf'
            # print(res_name)
            shutil.move(pdf_dir+'/'+fn, pdf_dir + '/'+ res_name)

            print("{} ---> {}".format(fn, res_name))

print('time cost: {}'.format(time.time() - start))


