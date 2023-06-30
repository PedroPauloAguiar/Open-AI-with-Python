from PyPDF2 import PdfMerger

merger = PdfMerger()

input1 = open("pdf/text1.pdf", "rb")
input2 = open("pdf/text2.pdf", "rb")

# Adicionar os dois arquivos PDF para o objeto merger
merger.append(fileobj=input1)
merger.append(fileobj=input2)

# Definir o nome do arquivo de saída
output = open("merged_output.pdf", "wb")

# Escrever o arquivo de saída
merger.write(output)
