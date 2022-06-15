import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for k, v in balls.items():
            self.contents += v * [k]

    def draw(self, num):
        num = min(num, len(self.contents))
        balls = []
        for x in range(num):
            ind = random.randint(0, len(self.contents)-1)
            balls.append(self.contents.pop(ind))
        return balls

def experiment(hat, bolas_esperadas, num_bolas_des, numeros_experiment):
    M = 0
    for _ in range(numeros_experiment):
        a_hat = copy.deepcopy(hat)
        balls = a_hat.draw(num_bolas_des)
        cores_certas = 0
        for cor in bolas_esperadas.keys():
            if balls.count(cor) >= bolas_esperadas[cor]:
                cores_certas += 1
        if cores_certas == len(bolas_esperadas):
            M += 1
    probability = float(M) / numeros_experiment
    return probability