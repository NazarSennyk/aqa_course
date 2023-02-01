class Iterator:
    def __init__(self, sequence, start_index=0, end_index=0):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index < len(self.sequence):
            item = self.sequence[self.start_index]
            self.start_index += 1
            return item
        else:
            raise StopIteration









