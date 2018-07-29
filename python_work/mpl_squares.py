import matplotlib.pyplot as plt

# 绘制简单的折线图
input_values = [1,2,3,4,5,6,7,8,9,10,11]
squares = [1,4,9,16,25,36,49,64,81,100,121]
# plt.plot(squares, linewidth=5)
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Squares of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize = 14)

plt.show()

