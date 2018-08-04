from die import Die

# 创建一个 D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100):
	result = die.roll()
	results.append(result)

print(results)