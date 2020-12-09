class CalculateData:
    candidates = []
    results = {}

    def __init__(self, candidates):
        candidates.pop(0)
        self.candidates = candidates
        self.calculate()

    def calculate(self):
        jobs = []
        for candidate in self.candidates:
            if candidate['puesto'] != '':
                jobs.append(candidate['puesto'])
        jobs = list(dict.fromkeys(jobs))

        resume = {}
        for job in jobs:
            resume[job] = []

        for candidate in self.candidates:
            for job in jobs:
                if candidate['puesto'] in job:
                    resume[job].append(candidate)

        results = {}
        for job in jobs:
            age = 0
            salary = ''
            job_candidates = 0
            for can in resume[job]:
                age = age + int(can['edad'])
                salary = int(can['salario'])
                job_candidates = job_candidates + 1

            prom = (age/len(resume[job]))

            results[job] = {
                'Candidatos': job_candidates,
                'Edad Promedio': prom,
                'Pretension Salarial': salary
            }
        self.results = results
        print('Calculated!')

    def evaluate_data(self):
        valid_candidates = []
        i = 0
        for candidate in self.candidates:
            if i == 0:
                valid_candidates.append(candidate)
            repeated = False
            for candi in valid_candidates:
                if candidate == candi:
                    repeated = True
            if not repeated:
                valid_candidates.append(candidate)

            i = i + 1
