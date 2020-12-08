from components.ReadCSVFiles import Read
from components.CalculateData import CalculateData


class Main:
    candidates = []

    def __init__(self):
        self.print_menu()

    def print_menu(self):
        while True:
            print('''
=================================================================================================================
                                        Welcome to Easy Solution App
Select an option:
1. Read CSV file
2. Calculate data
3. Generate JSON file
4. Exit
\n''')
            option = input()
            if option in '1':
                self.readCSVFile()
            elif option in '2':
                self.calculateData()
            elif option in '3':
                self.generateJson()
            elif option in '4':
                print('Bye bye')
                break

    def readCSVFile(self):
        file = Read()
        self.candidates = file.candidates

    def calculateData(self):
        print('Calculate data')
        if len(self.candidates) != 0:
            calculate = CalculateData(self.candidates)
        else:
            print('There are no candidates')

    def generateJson(self):
        print('generate json')


m = Main()
