class pdf:
    def read_pdf(self):
        return "Reading PDF file"
class word:
    def read_word(self):
        return "Reading Word file"
class excel:
    def read_excel(self):
        return "Reading Excel file"
pdf = pdf()
word = word()
excel = excel()
print(pdf.read_pdf())
print(word.read_word())
print(excel.read_excel())