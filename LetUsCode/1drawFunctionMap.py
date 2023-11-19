# 导入模块

import numpy as np # 导入numpy模块 ，数学计算库
import matplotlib.pyplot as plt  #绘图库

# 创建 x 值数组
x = np.linspace(-10, 10, 400)

# 定义函数
y = 2 * x**2 + 5 * x - 8

# 绘制图形
plt.plot(x, y)  # 绘制图形
plt.xlabel('x') # x,y轴标签
plt.ylabel('y') # x,y轴标签
plt.title('HanShu: y=2*X*X+5X+8') # 标题
plt.show() # 显示图形