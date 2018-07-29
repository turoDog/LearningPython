import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values, y_values, s = 100)

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

# plt.scatter(2, 4, s = 200)

# 设置图表标题并给坐标轴加上那个标签
plt.title("Squares Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis = "both", which = "major", labelsize = 14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()