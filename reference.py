import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import itertools

def HandB (Answer, Correct_Answer, M):
    H, B = 0, 0
    for i in range(M):
        if Answer[i] == Correct_Answer[i]:
            H = H + 1
        if Answer[i] in Correct_Answer:
            B = B + 1
    B = B - H
    return H, B

def check (Guess, Candicates, M, HB):
    Eliminated_Candicates = []
    for i in Candicates:
        result = HandB(Guess, i, M)
        if HB == result:
            Eliminated_Candicates.append(i)
    return Eliminated_Candicates

def game(N, M, Correct_Answer, flag_print=False):
    if (flag_print):
        print('-------------------------------------------------')
        print('Correct Answer : ' + ''.join(map(str, Correct_Answer)))

    Candicates = list(itertools.permutations(np.arange(N, dtype=int), M))
    Turn = 0
    HB = (0, 0)

    while (HB[0] != M):
        Turn += 1
        Guess = Candicates[np.random.default_rng().integers(len(Candicates))]
        HB = HandB(Guess, Correct_Answer, M)
        if (flag_print):
            print('-------------------------------------------------')
            print('Turn : ' + str(Turn))
            print('Candicates : ' + str(len(Candicates)))
            print('Guess : ' + ''.join(map(str, Guess)))
            print('Hit : ' + str(HB[0]))
            print('Blow : ' + str(HB[1]))
        Candicates = check(Guess, Candicates, M, HB)
    if (flag_print):
        print('-------------------------------------------------')
    return Turn