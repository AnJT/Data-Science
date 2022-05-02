import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

theta = np.arange(0,2 * np.pi, 0.01)
r = (1 - np.sin(theta))
x = r * np.cos(theta) 
y = r * np.sin(theta)
plt.plot(x, y, c="r", lw=5, ls='-.', label='Heart line')
# 1-1: 改用scatter函数控制输出
plt.scatter(x, y, c="g")
# 1-2: 改用极坐标控制输出:
# plt.polar(theta, r, color='r')
plt.legend(bbox_to_anchor=(1, 1.15))
plt.title('Heart Curve')
plt.show()


