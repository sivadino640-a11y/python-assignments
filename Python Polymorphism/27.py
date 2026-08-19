class ExcelReport:
    def generate(self):
        print("Generating Excel report")
class PDFReport:
    def generate(self):
        print("Generating PDF report")
def generate_report(report):
    report.generate()
excel = ExcelReport()
pdf = PDFReport()
generate_report(excel)
generate_report(pdf)