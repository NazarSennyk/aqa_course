from proxy.abstract_reader import Reader
from proxy.txt_reader import TxtReader


class TxtProxyReader(Reader):
    def __init__(self, txt_reader: TxtReader, file_path):
        self.result = ''
        self.is_actual = False
        self.reader = txt_reader
        self.file_path = file_path

    def read_file(self):
        if self.is_actual:
            return self.result
        else:
            self.result = self.reader.read_file()
            self.is_actual = True
            return self.result

    def write_file_change_actual(self, new_data):
        if self.is_actual:
            return self.is_actual
        else:
            with open(self.file_path) as file:
                text = file.write(new_data)
                self.is_actual = False
                return text



