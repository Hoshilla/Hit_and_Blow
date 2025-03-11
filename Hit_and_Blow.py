import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
import itertools
from reference import *

M = 4 #選ぶ数字カードの枚数.
N = 10 #選ぶ元となる数字の個数.

Turns = []
Calc = 40000 #計算回数.
Correct_Answers = []
print('----Calculating---------------------------------------------')
for i in range(Calc):
    #正解をランダム生成.
    Correct_Answer = np.random.default_rng().permutation(N)[0:M]
    Correct_Answers.append(Correct_Answer)
    Turns.append(game(N, M, Correct_Answer))
    if i % 1000 == 0:
        print('{:.2f}'.format(100*i/Calc) + ' %')

""" #全ての正解パターンを計算.
print('----Calculating---------------------------------------------')
Correct_Answers = list(itertools.permutations(np.arange(N, dtype=int), M))
for i, Corrects in enumerate(Correct_Answers):
    Turns.append(game(N, M, Corrects))
    if i % 1000 == 0:
        print('{:.2f}'.format(100*i/len(Correct_Answers)) + ' %') """

ndarray_Turns = np.array(Turns)
print('-------------------------------------------------')
print('Ave = ' + '{:.4f}'.format(np.average(ndarray_Turns)))
print('Max = ' + '{:.4f}'.format(np.max(ndarray_Turns)))
print('Min = ' + '{:.4f}'.format(np.min(ndarray_Turns)))
print('Var = ' + '{:.4f}'.format(np.var(ndarray_Turns)))
print('-------------------------------------------------')
print('強い数たち')
maxIndex = [print(''.join(map(str, Correct_Answers[i]))) for i, x in enumerate(ndarray_Turns) if x==max(ndarray_Turns)]

#フォント
plt.rcParams['font.size'] = 12
plt.rcParams['font.family']= 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
#軸
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.2
plt.rcParams['ytick.major.width'] = 1.2
plt.rcParams['axes.linewidth'] = 1.2
#凡例
plt.rcParams['legend.markerscale'] = 2
plt.rcParams['legend.fancybox'] = False
plt.rcParams['legend.framealpha'] = 1
plt.rcParams['legend.edgecolor'] = 'black'
colors = {'red':'#FF4B00','blue':'#005AFF','green':'#03AF7A','cyan':'#4DC4FF','orange':'#F6AA00','yellow':'#FFF100','black':'#000000'}
keys = ['red', 'blue', 'orange', 'green', 'cyan', 'yellow', 'black']

fig = plt.figure(figsize=(5, 5), dpi=300)
ax = fig.add_subplot(111)
plt.bar(np.arange(np.max(ndarray_Turns)), np.unique(ndarray_Turns, return_counts=True)[1],
         color='#4DC4FF', edgecolor='black', align='center')
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_xlim(0,)
ax.xaxis.set_major_locator(MultipleLocator(1))
#ax.set_ylim()
#ax.legend()
# save
fig.savefig('数字{:}個から{:}個(Guess=random).png'.format(N,M), bbox_inches='tight', pad_inches=0.05, transparent=False)
