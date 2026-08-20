class File:
    def read(self):
        pass
    def write(self):
        pass
class TextFile(File):
    def read(self):
        print("Reading text file")
    def write(self):
        print("Writing text file")
class CSVFile(File):
    def read(self):
        print("Reading CSV file")
    def write(self):
        print("Writing CSV file")
TextFile().read()
TextFile().write()
CSVFile().read()
CSVFile().write()