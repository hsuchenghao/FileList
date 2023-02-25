import matplotlib.pyplot as plt
import numpy as np

# 设置画布大小为 6x4 英寸
fig = plt.figure(figsize=(6, 4))
# 设置画布背景色为纯白色
fig.patch.set_facecolor('white')

# 添加一个绘图子区域
ax = fig.add_subplot(1, 1, 1)

# 绘制底色为白色的矩形
ax.add_patch(plt.Rectangle((0, 0), 1, 1, color='white'))

# 绘制月亮和星星
theta = np.linspace(0, 2 * np.pi, 200)
x = 0.5 + 0.2 * np.cos(theta)
y = 0.5 + 0.2 * np.sin(theta)
ax.fill(x, y, 'navy')
ax.fill(x + 0.15, y + 0.15, 'white')

# 绘制绿色带子
ax.add_patch(plt.Rectangle((0.8, 0), 0.2, 1, color='green'))

# 隐藏坐标轴
ax.set_axis_off()

# 保存图片为 ftly.png
plt.savefig('ftly.png', dpi=300, bbox_inches='tight')
