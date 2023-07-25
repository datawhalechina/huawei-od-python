def calculate_max_profit(input_str):
	# 如果输入字符串为空，则返回0
	if not input_str:
		return 0

	#将输入字符串按空格分割成字符串列表
	price_strings = input_str.split()
	# 初始化价格列表，长度为价格字符串列表的长度，每个元素都为0
	prices = [0] * len(price_strings)

	# 遍历价格字符串列表
	for i in range(len(price_strings)):
		#取出当前价格字符串
		price_string = price_strings[i]
		# 如果价格字符串的最后一个字符不是数字， 则说明输入无效，返回0
		if not price_string[:-1].isdigit():
			return 0
		# 将价格字符串转换为整数
		value = int(price_string[:-1])
		# 取出价格字符串的最后一个字符，判断货币类型
		currency = price_string[-1]
		# 如果货币类型是"S",则将价格乘以7
		if currency == "S":
			value *= 7
		# 将处理后的价格存入价格列表
		prices[i] = value


	#初始化最大利润为0
	max_profit = 0

	#遍历价格列表，计算最大利润
	for i in range(1, len(prices)):
		# 如果当前价格比前一个价格高，则将差值加入最大利润
		if prices[i] > prices[i - 1 ]:
			max_profit += prices[i] - prices[i - 1]


	# 返回最大利润
	return max_profit

# 读取输入字符串，并计算最大利润
input_str = input()
print(calculate_max_profit(input_str))



