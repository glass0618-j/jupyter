def frequency(toeicScores):
    counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for toeicScore in toeicScores:
        counters[toeicScore//100] += 1
    return counters

def max_frequency(counters):
    max = 0
    scoreBase = 0
    N = len(counters)
    for i in range(N):
        if max < counters[i]:
            max = counters[i]
            scoreBase = i * 100
    return scoreBase, max

def min_frequency(counters):
    scoreBase = 0
    N = len(counters)
    min = 11
    for i in range(N):
        if counters[i] !=0 and min > counters[i]:
            scoreBase = i * 100
            min = counters[i]
    return scoreBase, min

toeicScores = [510, 630, 750, 780, 620, 805, 890, 650, 840, 670]

counters = frequency(toeicScores)
#scoreBase 
