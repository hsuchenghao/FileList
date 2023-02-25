import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# 绘制蓝色背景矩形
ax.add_patch(plt.Rectangle((0, 0), 1, 1, color='blue'))

# 绘制白色太阳底座
ax.add_patch(plt.Rectangle((0.35, 0.45), 0.3, 0.1, color='white'))

# 绘制太阳光芒
ax.plot([0.5, 0.15], [0.5, 0.7], color='white', linewidth=7)
ax.plot([0.5, 0.85], [0.5, 0.7], color='white', linewidth=7)
ax.plot([0.5, 0.3], [0.5, 0.3], color='white', linewidth=7)
ax.plot([0.5, 0.7], [0.5, 0.3], color='white', linewidth=7)

# 绘制红色太阳
ax.add_patch(plt.Circle((0.5, 0.5), 0.15, color='red'))

# 设置坐标轴范围
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

# 隐藏坐标轴
ax.axis('off')

# 保存图像
plt.savefig('roc.png', dpi=300, bbox_inches='tight')
