import matplotlib.pyplot as plt

# 绘制前5000个整数立方值的散点图

x_values=list(range(1,5000))
y_values=[x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上那个标签
plt.title("Cubes Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubes of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis = "both", which = "major", labelsize = 14)

plt.show()