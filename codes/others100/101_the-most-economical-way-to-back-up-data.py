# 解法一
#def can_allocate(files, num_boxes):
# 	#创建一个长度为num_boxes的光盘列表，初始值为500
# 	box_capacities = [500] * num_boxes
	
# 	#文件列表中的最后一个文件开始分配
# 	for file in reversed(files):
# 		#对光盘容量进行排序，确保每次选择容量最小的箱子进行分配
# 		box_capacities.sort()

# 		#检查最大容量的光盘是否能够容纳当前文件
# 		if box_capacities[num_boxes - 1] >= file:
# 			box_capacities[num_boxes - 1] -= file
# 		else:
# 			#如果最大容量的光盘无法容纳当前文件，则无法完成分配
# 			return False


# 	#如果能够成功分配所有文件，则返回True
# 	return True

# def solve_method():
# 	#分隔的文件列表 并转换为整数数组
# 	files = list(map(int, input().split(",")))
# 	files.sort() # 对文件列表进行排序

# 	min_boxes = 0
# 	max_boxes = len(files) + 1

# 	#使用二分查找确定最小的光盘数量
# 	while min_boxes < max_boxes:
# 		mid = (min_boxes + max_boxes) // 2
# 		if can_allocate(files, mid):
# 			#如果能够完成分配，则缩小光盘数量的上限
# 			max_boxes = mid
# 		else:
# 			#如果无法完成分配，则增加光盘数量的下限
# 			min_boxes = mid + 1

# 	print(min_boxes)
# if __name__ == "__main__":
# 	solve_method()

#解法二
def solve_method(arr, num):
	if len(arr) <=1:
		print(num)
		print(arr)
		print(num+len(arr))
		return num+len(arr)
	else:
		if arr[0]+arr[-1]<500:
			arr[-1]+=arr[0]
			arr.pop(0)
		else:
			if arr[0]+arr[-1]==500:
				arr.pop()
				arr.pop(0)
			else:
				arr.pop()
			num+=1
		solve_method(arr,num)

if __name__ == "__main__":
	files = list(map(int, input().split(",")))
	files.sort()
	solve_method(files,0)