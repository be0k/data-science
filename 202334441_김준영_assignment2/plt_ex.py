import numpy as np
from matplotlib import pyplot as plt
np.random.seed(42)
wt = np.random.random(100) * 50 + 40
ht = np.floor(np.random.random(100) * 60 + 140).astype(np.int32)
bmi = wt * 10000 / (ht * ht)

x = ['Underweight', 'Healthy', 'Overweight', 'Obese']
tmp = np.digitize(bmi, bins = [-np.inf, 18.5, 25, 30, np.inf])
cnt = np.unique(tmp,return_counts=True)[1]

plt.subplot(221)
plt.xticks(rotation=20)
plt.bar(x, cnt, color = ['r','g','b','orange'])

plt.subplot(222)
plt.hist(bmi,bins = [400000 / (190 * 190), 18.5, 25, 30, 900000 / (140 * 140)])

plt.subplot(223)
plt.pie(cnt, labels = x, autopct='%1.1f%%')

plt.subplot(224)
plt.scatter(ht[tmp==1], wt[tmp==1])
plt.scatter(ht[tmp==2], wt[tmp==2])
plt.scatter(ht[tmp==3], wt[tmp==3])
plt.scatter(ht[tmp==4], wt[tmp==4])
'''
#original
plt.scatter(ht, wt)
'''

plt.show()

