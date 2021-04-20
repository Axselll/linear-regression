import pandas as pd
import numpy as np

np.random.seed(0)
x = np.random.rand(100, 1)  # membuat nomor acak untuk variabel x
y = 2 + 3 * x + np.random.rand(100, 1)  # sama kayak x cuman untuk y
print(x[:10], y[:10])  # menampilkan 10 baris pertama dari x dan y
