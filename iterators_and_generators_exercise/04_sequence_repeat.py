class sequence_repeat:
    def __init__(self, sequence, number):
        self.number = number
        self.sequence = sequence
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        temp = self.sequence[self.current_index]
        self.current_index += 1
        self.number -= 1
        if self.current_index == len(self.sequence):
            self.current_index = 0
        return temp


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
