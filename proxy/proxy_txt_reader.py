from proxy.abstract_reader import Reader
from proxy.txt_reader import TxtReader
from proxy.txt_writer import TxtWriter


class TxtProxyReaderWriter(Reader):
    def __init__(self, txt_reader: TxtReader, txt_writer: TxtWriter):
        self.result = ''
        self.is_actual = False
        self.reader = txt_reader
        self.writer = txt_writer

    def read_file(self):
        if self.is_actual:
            return self.result
        else:
            self.result = self.reader.read_file()
            self.is_actual = True
            return self.result

    def write_file(self):
        if self.is_actual is False:
            return self.is_actual
        else:
            self.result = self.writer.write_file('some_file')
            self.is_actual = False
            return self.result










