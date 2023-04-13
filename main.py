import PyPDF4

file1 = input('Quais os nomes dos arquivos\n') + '.pdf'
file2 = input('Quais os nomes dos arquivos\n') + '.pdf'
output_file_name = input('Qual o nome do arquivo de saída\n') + '.pdf'

pdf1 = open(file1, 'rb')
pdf2 = open(file2, 'rb')

pdf1_reader = PyPDF4.PdfFileReader(pdf1)
pdf2_reader = PyPDF4.PdfFileReader(pdf2)

pdf_writer = PyPDF4.PdfFileWriter()

for page_num in range(pdf1_reader.numPages):
    page = pdf1_reader.getPage(page_num)
    pdf_writer.addPage(page)

for page_num in range(pdf2_reader.numPages):
    page = pdf2_reader.getPage(page_num)
    pdf_writer.addPage(page)

output_file = open(output_file_name, 'wb')
pdf_writer.write(output_file)

pdf1.close()
pdf2.close()
output_file.close()


