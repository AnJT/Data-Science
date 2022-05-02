from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

R = 10
r = R * np.sin(np.pi / 10) / np.sin(np.pi / 5)
DG = 0

def rad(x):
    return x * np.pi / 180

fig = plt.figure(figsize=(8, 8), dpi=72)
plt.xticks(np.linspace(-10, 10, 5))
plt.yticks(np.linspace(-10, 10, 5))
plt.title ("红五角星")

out_x = [R * np.cos(rad(90 + k * 72 + DG)) for k in range(6)]
out_y = [R * np.sin(rad(90 + k * 72 + DG)) for k in range(6)]
in_x = [r * np.cos(rad(90 + 36 + k * 72 + DG)) for k in range(6)]
in_y = [r * np.sin(rad(90 + 36 + k * 72 + DG)) for k in range(6)]
x, y = [], []
for i in range(6):
    x.extend([out_x[i], in_x[i]])
    y.extend([out_y[i], in_y[i]])

plt.plot(out_x, out_y, color='y')
plt.plot(in_x, in_y, color='w')
plt.plot(x, y, color='r')
plt.fill(x, y, color='r')
theta = np.arange(0, 2 * np.pi, 0.01)
plt.plot(r * np.sin(theta), r * np.cos(theta), color='g')
plt.plot(R * np.sin(theta), R * np.cos(theta), color='b')
plt.scatter(in_x, in_y, color='b', lw=10)
plt.scatter(out_x, out_y, color='r', lw=10)
plt.show()
