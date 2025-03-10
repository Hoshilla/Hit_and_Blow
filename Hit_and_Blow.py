import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

M = 3 #選ぶ数字カードの枚数.
N = 10 #選ぶ元となる数字の個数.
Correct_global = np.random.default_rng().integers(N, size=M)
print(Correct_global)