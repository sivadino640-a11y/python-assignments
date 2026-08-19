class Printer:
    def print(self):
        print("Printing document")
class PDFPrinter:
    def print(self):
        print("Printing PDF document")
def start_printing(printer):
    printer.print()
p = Printer()
pdf = PDFPrinter()
start_printing(p)
start_printing(pdf)