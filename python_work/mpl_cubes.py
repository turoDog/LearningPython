import matplotlib.pyplot as plt

# 绘制前五个整数的散点图

x_values = [1,2,3,4,5]
cubes = [x**3 for x in x_values]

# 设置图表标题，并给坐标轴加上标签
plt.title("Cube Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Cube of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize = 14)

plt.plot(x_values, cubes, c=(0,0,1), linewidth=5)

plt.show()