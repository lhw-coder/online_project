"""
两层的神经网络
两个激活函数
1。tanh函数
2。soft——max函数
x 为输入的每一张图片；
b0\w0\b1  未知参数
a = tanx + b0
b = softmax(w0*a+b1)  放大特征像素
feature = 求和w(i,j)*Xj + bi

cross_entropy:损失函数为模型的优化方向
结果的预测的概率分布和结果的真实的概率分布
(y - y`) ** 2 = L   ---> loss function
梯度下降算法：求偏导数
求极值即可。调整参数，使德loss达到最优。


主要思想是：
某类的特征加权求和，而权重是模型根据自动学习、训练来的
如果某个像素的灰度值代表的就是可能是数字n，权重就越大，反之，权重可能是负的
"""
import math
a = math.atan(0)
print(a)
b = math.tan(1.572)
print(b)
