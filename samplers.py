import matplotlib.pyplot as plt
import random
import sys

def uniform(n):
    ret = []
    for i in range(n * n):
        x = random.random()
        y = random.random()
        ret.append([x, y])
    return ret

def jittered(n):
    ret = []
    for i in range(n):
        for j in range(n):
            x = (j + random.random()) / n
            y = (i + random.random()) / n
            ret.append([x, y])
    return ret

def shuffle(points, k):    
    for i in range(len(points)):
        j = random.randrange(len(points))
        points[i][k], points[j][k] = points[j][k], points[i][k]

def nrocks(n):
    ret = []
    for i in range(n * n):
        x = (i + random.random()) / (n * n)
        y = (i + random.random()) / (n * n)
        ret.append([x, y])
    shuffle(ret, 0)
    shuffle(ret, 1)
    return ret

def multi_jittered(n):
    ret = []
    for i in range(n):
        for j in range(n):
            x = (j * n + i + random.random()) / (n * n)
            y = (i * n + j + random.random()) / (n * n)
            ret.append([x, y])
    for i in range(n):
        for j in range(n):
            ii = random.randrange(n)
            p = i * n + j
            q = ii * n + j
            ret[p][0], ret[q][0] = ret[q][0], ret[p][0]
    for i in range(n):
        for j in range(n):
            jj = random.randrange(n)
            p = i * n + j
            q = i * n + jj
            ret[p][1], ret[q][1] = ret[q][1], ret[p][1]

    return ret

def draw_samples(sampler, n):
    samples = sampler(n)
    plt.scatter([p[0] for p in samples], [p[1] for p in samples])
    plt.title(sampler.__name__)

def draw(n):
    fig = plt.figure()
    samplers = [uniform, jittered, nrocks, multi_jittered]
    for i in range(4):
        fig.add_subplot(2, 2, i + 1)
        draw_samples(samplers[i], n)
    plt.show()    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        draw(int(sys.argv[1]))
    else:
        draw(5)