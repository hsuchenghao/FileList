import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# 创建一个绘图窗口和子图对象
fig, ax = plt.subplots(figsize=(6, 4))

# 设置国旗底色
ax.set_facecolor('navy')

# 绘制月亮
moon_center = (0.5, 0.5)
moon_radius = 0.4
moon_color = '#d1c1ee'
moon = Circle(moon_center, moon_radius, color=moon_color)
ax.add_artist(moon)

# 绘制星星
star_color = 'white'
star_points = [(0.46, 0.42), (0.48, 0.35), (0.5, 0.42), (0.52, 0.35), (0.54, 0.42),
               (0.54, 0.47), (0.5, 0.44), (0.46, 0.47), (0.46, 0.42)]
for point in star_points:
    star = Circle(point, 0.025, color=star_color)
    ax.add_artist(star)

# 隐藏坐标轴刻度和边框
ax.set_xticks([])
ax.set_yticks([])
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

# 保存图像到本地文件
plt.savefig('flag.png', bbox_inches='tight', pad_inches=0, dpi=300)

# 显示绘图
plt.show()
