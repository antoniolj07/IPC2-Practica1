class CalculateData:
    candidates = []

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
        print(jobs)

        resume = {}
        for job in jobs:
            resume[job] = []

        for candidate in self.candidates:
            for job in jobs:
                if candidate['puesto'] in job:
                    resume[job].append(candidate)

        print(resume)

        results = {}
        for job in jobs:
            age = 0
            salary = ''
            job_candidates = 0
            for can in resume[job]:
                age = age + int(can['edad'])
                salary = can['salario']
                job_candidates = job_candidates + 1

            prom = (age/len(resume[job]))

            results[job] = {
                'Edad Promedio': prom,
                'Pretension Salarial': salary,
                'Candidatos': job_candidates

            }

        print(results)
