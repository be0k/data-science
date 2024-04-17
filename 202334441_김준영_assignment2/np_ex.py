import numpy as np
np.random.seed(42)

wt = np.random.random(100) * 50 + 40
ht = np.floor(np.random.random(100) * 60 + 140).astype(np.int32)
bmi = wt * 10000 / (ht * ht)
print(bmi)

