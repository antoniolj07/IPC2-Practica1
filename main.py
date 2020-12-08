from components.ReadCSVFiles import Read

class Main:
    def __init__(self):
        self.printMenu()

    def printMenu(self):
        while (True):
            print('''
=================================================================================================================
                                        Welcome to Easy Solution App
Select any option:
1. Read CSV file
2. Calculate data
3. Generate JSON file
4. Exit
            ''')
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
        print('read csv')
        file = Read()

    def calculateData(self):
        print('Calculate data')

    def generateJson(self):
        print('generate json')


m = Main()
