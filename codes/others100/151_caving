import re
# 该代码首先使用正则表达式从输入数据中提取所有的坐标，并进行合法性判断。然后计算每个坐标相对于总部的距离，并找到距离最大的坐标。最后返回最远足迹到达的坐标。如果输入数据中没有合法的坐标，则返回总部坐标(0,0)。

def get_farthest_coordinate(data):
    coordinates = re.findall(r'\((\d+),(\d+)\)', data)
    valid_coordinates = []
    for coordinate in coordinates:
        x, y = map(int, coordinate)
        if 0 < x < 1000 and 0 < y < 1000:
            valid_coordinates.append((x, y))
    if len(valid_coordinates) == 0:
        return "(0,0)"

    distances = [x ** 2 + y ** 2 for x, y in valid_coordinates]
    max_distance_index = distances.index(max(distances))
    return f"({valid_coordinates[max_distance_index][0]},{valid_coordinates[max_distance_index][1]})"


data = input()
result = get_farthest_coordinate(data)
print(result)
