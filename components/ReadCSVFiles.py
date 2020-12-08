class Read:
    def __init__(self):
        self.readFile()

    def readFile(self):
        path = input('Please enter the path of the CSV file')
        with open(path, 'r') as f:
            lines = f.readlines()
            print(lines)
            rows = []
            for line in lines:
                row = ''
                for x in range(len(line)):
                    if not line[x] in '/n':
                        row = row + line[x]
                        