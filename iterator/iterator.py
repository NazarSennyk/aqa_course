class Iterator:
    def __init__(self, sequence, start_index: int, end_index: int):
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
        if self.end_index < 0:
            raise StopIteration


