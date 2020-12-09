from components.ReadCSVFiles import Read
from components.CalculateData import CalculateData
from components.createJSON import CreateFile


class Main:
    candidates = []
    results = {}

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
                self.read_csv_file()
            elif option in '2':
                self.calculate_data()
            elif option in '3':
                self.generate_json()
            elif option in '4':
                print('Bye bye')
                break
            else:
                print('Please enter a valid option')

    def read_csv_file(self):
        file = Read()
        self.candidates = file.candidates

    def calculate_data(self):
        print('Calculate data')
        if len(self.candidates) != 0:
            calculate = CalculateData(self.candidates)
            self.results = calculate.results
        else:
            print('There are no candidates!')

    def generate_json(self):
        if len(self.results.keys()) != 0:
            create = CreateFile(self.results)
        else:
            print('First you should calculate the data!')


m = Main()
