import csv

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            with open(filename) as f:
                csvreader = csv.reader(f, delimiter=sep)

                # for row in csvreader:
                #     print(row)

                data_iter = iter(csvreader)

                if header:
                    self.header = next(data_iter)
                else:
                    self.header = None

                self.data = list(data_iter)[skip_top:]
                if skip_bottom:
                    self.data = self.data[:-skip_bottom]

            self.corrupted = False
        except Exception:
            self.corrupted = True


    def __enter__(self):
        if self.corrupted:
            return None
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


    def getdata(self):
        if self.corrupted:
            return None

        return self.data

    def getheader(self):
        if self.corrupted:
            return None

        return self.header




if __name__ == "__main__":
    with CsvReader('good.csv', header=True, skip_top=3, skip_bottom=2) as file:
        data = file.getdata()
        header = file.getheader()
        header = file.getheader()
        


if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")

