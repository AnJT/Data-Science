from matplotlib import pyplot as plt
import numpy as np
plt.rcParams['axes.unicode_minus'] = False 

def draw(x, y, a, color, marker):
    plt.xticks(x)
    plt.yticks(y)
    plt.title(f'a={a}')
    theta = np.arange(0, 2 * np.pi, 0.02)
    r = np.sin(a * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.scatter(x, y, c=color, marker=marker)

a = [1.5, 3, 5, 2, 4, 6]
colors = ['b', 'b', 'b', 'g', 'g', 'g']
markers = ['p', 'p', 'p', '^', '^', '^']
fig = plt.figure(figsize=(12, 8), dpi=72)
for i in range(6):
    plt.subplot(2, 3, i+1)
    x = np.linspace(-1, 1, 5) if i else np.linspace(0, 1, 5)
    y = np.linspace(-1, 1, 5)
    draw(x, y, a[i], colors[i], markers[i])
plt.show()