class Read:
    candidates = []

    def __init__(self):
        self.read_file()

    def read_file(self):
        path = input('Please enter the path of the CSV file \n')
        rows = []
        try:
            with open(path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    row = ''
                    for x in range(len(line)):
                        if not line[x] in '\n':
                            row = row + line[x]
                    rows.append(row)
            self.read_attributes(rows)
        except:
            print('Something went wrong :(')

    def read_attributes(self, rows):
        candidates = []
        for row in rows:
            candidate = {
                'id': '',
                'nombre': '',
                'apellido': '',
                'edad': '',
                'puesto': '',
                'salario': ''
            }
            e = 0
            for x in range(len(row)):
                if e == 0:
                    if not row[x] in ',':
                        candidate['id'] = candidate['id'] + row[x]
                    else:
                        e = 1
                elif e == 1:
                    if not row[x] in ',':
                        candidate['nombre'] = candidate['nombre'] + row[x]
                    else:
                        e = 2
                elif e == 2:
                    if not row[x] in ',':
                        candidate['apellido'] = candidate['apellido'] + row[x]
                    else:
                        e = 3
                elif e == 3:
                    if not row[x] in ',':
                        candidate['edad'] = candidate['edad'] + row[x]
                    else:
                        e = 4
                elif e == 4:
                    if not row[x] in ',':
                        candidate['puesto'] = candidate['puesto'] + row[x]
                    else:
                        e = 5
                elif e == 5:
                    if not row[x] in ',':
                        candidate['salario'] = candidate['salario'] + row[x]
                    else:
                        e = 0
            candidates.append(candidate)
        valid_candidates = []
        i = 0
        for candidate in candidates:
            if i == 0:
                valid_candidates.append(candidate)
            repeated = False
            for candi in valid_candidates:
                if candidate == candi:
                     repeated = True
            if not repeated:
                valid_candidates.append(candidate)

            i = i + 1
        self.print_candidates(valid_candidates)

    def print_candidates(self, candidates):
        for candidate in candidates:
            print('''
id:         {}
nombre:     {}
apellido:   {}
edad:       {}
puesto:     {}
salario:    {}
            '''.format(candidate['id'], candidate['nombre'], candidate['apellido'], candidate['edad'], candidate['puesto'], candidate['salario']))

        self.candidates = candidates
