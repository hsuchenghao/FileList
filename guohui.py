import matplotlib.pyplot as plt
import numpy as np

# 创建画布
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# 设置背景颜色为白色
fig.set_facecolor('white')

# 绘制圆形
circle = plt.Circle((0, 0), 0.5, color='red')
ax.add_artist(circle)

# 绘制太极图案
yin_yang = plt.Circle((0, 0), 0.2, color='white')
yang = plt.Rectangle((-0.1, 0), 0.2, 0.2, color='black')
yin = plt.Rectangle((-0.1, -0.2), 0.2, 0.2, color='white')
ax.add_artist(yin_yang)
ax.add_artist(yang)
ax.add_artist(yin)

# 绘制“奉天璃月”字样
text = plt.text(0, -0.6, '奉天璃月', fontsize=20, ha='center')

# 设置坐标轴范围
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# 隐藏坐标轴
plt.axis('off')

# 保存图片
plt.savefig('guohui.png')
