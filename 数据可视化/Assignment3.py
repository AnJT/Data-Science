from matplotlib import pyplot as plt
import numpy as np

v1 = [0.833*4.5, 0.737*3.7, 0.769*5.0, 0.68*3.1]
v2 = [0.167*4.5, 0.263*3.7, 0.231*5.0, 0.32*3.1]
v3 = [i + j for i, j in zip(v1, v2)]
v4 = [i * 100 / j for i, j in zip(v1, v3)]
v5, v6 = [2, 5, 3, 8], [10, 14, 10, 17]
xtk = ['Metabolism/homeostasis\n & Nervous system', 
    'Metabolism/homeostasis\n & Respiratory system', 
    'Nervous system\n & Congenital anomalies', 
    'Congenital anomalies \n& Feeding difficulties\n']

index = np.arange(4)
bar_width = 0.5
fig, ax = plt.subplots()
plt.bar(index, v1, bar_width, color='#082567', label='Individuals with a molecular diagnosis')
plt.bar(index, v2, bar_width, bottom=v1, color='#B0C4DE', label='Individuals Without a molecular diagnosis')

for i in range(4):
    x = index[i]
    plt.text(x, v3[i]+0.05, '%.1f' %v3[i], ha='center', va='bottom')
    plt.text(x, v1[i]+v2[i]/2-0.15, '%d' %v5[i], ha='center', va='bottom')
    plt.text(x, v1[i]/2+0.15, '%d' %v6[i], color='w', ha='center', va='bottom')
    plt.text(x, v1[i]/2-0.3, '%4.1f%%' %v4[i], color='w', ha='center', va='bottom')

plt.xlabel('two affected system')
plt.xticks(index, xtk, rotation=30)
plt.ylabel('Adjusted Odds Ratio')
plt.yticks(np.arange(12), ['0','','2','','4','','','','','18','20','22'])
plt.legend(loc='upper right')
plt.show()