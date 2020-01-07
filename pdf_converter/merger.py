import sys
import PyPDF2

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(f'{pdf} merged')
        merger.append(pdf)
    merger.write(('merged_doc.pdf'))

pdf_combiner(inputs)
