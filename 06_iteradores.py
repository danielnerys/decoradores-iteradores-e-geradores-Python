
class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)
        self.lines = self.file.read().split(',')
        self.index = 0
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lines):
            line = self.lines[self.index].strip()
            self.index += 1
            return line
        else:
            raise StopIteration


lista_numeros = [int(line) for line in FileIterator('lista.txt')]

for item in lista_numeros:
    if item % 2 == 0:
        print(item)
