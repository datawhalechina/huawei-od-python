def solve_method(num):
	binary = bin(num)[2:]
	length = len(binary)
	builder = ""
	for i in range(length, 0, -7):
		start = max(i - 7, 0)
		bin_ = binary[start:i]
		if len(bin_) < 7:
			head = "0" * (7 - len(bin_))
			bin_= head + bin_
		bin_ = "0" + bin_ if i - 7 <= 0 else "1" + bin_
		hex_  = hex(int(bin_,2)).upper()[2:].zfill(2)
		builder += hex_

	print(builder)



if __name__ == "__main__":
	num = int(input().strip())
	solve_method(num)