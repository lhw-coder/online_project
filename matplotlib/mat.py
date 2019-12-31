import matplotlib.pyplot as plt

plt.plot([1,4,6,8],[3,4,5,8],marker='.',linestyle=':',color='b',label='x')
plt.plot([2,3,4,5],[1,2,3,4],label='y')
# latex语法
# plt.title("$x^2$")
plt.title('$\sum_{x=1}^{N}x^2$')
plt.xlabel("X")  # x轴的标签
plt.xlim(0,5)  # x轴的范围
plt.xticks([0,1,2,4]) # x的刻度
plt.legend() # 显示图例
plt.show()

import numpy as np
# 绘制函数图像
x = np.linspace(-100,100,10000)
y1 = x
y2 = x **2
y3 = 3*x**3 + 2*x**2 + 1
y4 = np.sin(x)

# 折线图
plt.plot(x, y1, label='$y=x$')
plt.plot(x, y2, label='$y=x^2$')
plt.plot(x, y3, label="$y=3x^3+2x^2+1$")
plt.plot(x, y4, label="$y=\sin{x}$")
plt.legend()
plt.ylim(-1,10)
plt.show()

# 柱状图
plt.bar([0,1,2,3],[5,10,15,18])
plt.xticks([0,1,2,3],['a','b','c','d'])
plt.show()