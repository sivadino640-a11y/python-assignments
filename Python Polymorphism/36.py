class TextFile:
    def read(self):
        print("Reading Text File")
class PDFFile:
    def read(self):
        print("Reading PDF File")
class ExcelFile:
    def read(self):
        print("Reading Excel File")
def read_file(file):
    file.read()
read_file(TextFile())
read_file(PDFFile())
read_file(ExcelFile())