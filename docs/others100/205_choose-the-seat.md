# 205 选座位

## 题目描述

疫情期间，需要大家保证一定的社交距离。公司组织开交流会议，座位有一排共`N`个座位，编号分别为[0,1,2,...,N-1]。要求员工一个接着一个进入会议室，并且还可以在任何时候离开会议室，每当一个员工进入时，需要坐到最大社交距离的座位。

例如：  
位置A与左右有员工落座的位置距离分别为2和2，位置B与与左右有员工落座的位置距离分别为2和3，影响因素都为两个位置，则认为作为A和B与左右位置的社交距离是一样的，如果有多个这样的座位，则坐到索引最小的那个座位。

## 输入描述

会议室座位总数的取值范围为1 <= seatNum <= 100，员工的进出顺序`seatOrLeave`数组元素值为1表示进场，元素值为负数表示出场（特殊：位置0的员工不会离开）。

例如：-4表示坐在位置4的员工离开（保证有员工坐在该座位上）。

## 输出描述

最后进来的员工，他会坐在第几个位置，如果位置已满，则输出-1。

## 示例描述

### 示例一

**输入：**
```text
10
[1,1,1,1,-4,1]
```

**输出：**
```text
5
```

**说明：**  
根据题意，按照员工进离场的顺序：
- `seat->0`：坐在任何位置都行，但要给他安排索引最小的位置，也就是座位0。
- `seat->9`：要和旁边的人距离最远，也就是座位9。
- `seat->4`：位置4与位置0、位置9的距离为4和5，位置5与位置0、位置9的距离为5和4，所以位置4和5都是可选的座位，按照要求需要选择索引最小的，所以选择座位4。
- `seat->2`：位置2与位置0、位置4的距离为2和2，位置6与位置4、位置9的距离为2和3，位置7与位置4、位置9的距离为3和2，按照要求需要选择索引最小的，所以选择座位2.
- `leave(4)`：4号座位员工离开
- `seat->5`：员工左后坐在5号座位。

## 解题思路

**基本思路：**
1. 初始化已占用的座位列表，`False`表示未占用。
2. 循环遍历员工进离场的顺序：
   - 遍历每一个未被占用的座位：如果座位没有被占用，计算与左右两边相邻的空座位的距离
        - 如果最左边的第0号座位没有人坐，计算距离和
        - 如果最右边的座位没有人坐，距离等于左边距离
        - 其他：计算距离和，并计算距离之差的绝对值
   - 排除掉所有相邻的座位，将座位编号、左右两边相邻的空座位的距离之和、距离之差的绝对值
3. 按照左右距离和降序，按距离之差的绝对值升序（保证处于中间位置），座位号升序进行排序
4. 取第一个座位编号并返回。

## 解题代码

```python
def solve_method(seatNum, seatOrLeave):
    order_seat = []
    # 已占用的座位
    used_seats = [False] * seatNum
    for i in range(len(seatOrLeave)):
        if seatOrLeave[i] > 0:
            available_seats = []
            for j in range(seatNum):
                if not used_seats[j]:
                    # 如果座位没有被占用，计算与左右两边相邻的空座位的距离
                    left_index, right_index = j, j
                    left_distance, right_distance = 0, 0
                    # 找到最左边的座位和距离
                    while left_index > 0 and not used_seats[left_index]:
                        left_distance += 1
                        left_index -= 1
                    # 找到最右边的座位和距离
                    while right_index < seatNum and not used_seats[right_index]:
                        right_distance += 1
                        right_index += 1
                    if not used_seats[0]:
                        # 最左边的第0号座位没有人坐
                        distance = left_distance + right_distance
                        distance_diff = -1
                    elif left_index >= 0 and not used_seats[seatNum - 1]:
                        # 最右边的座位没有人坐
                        distance = left_distance
                        distance_diff = -1
                    else:
                        distance = left_distance + right_distance
                        distance_diff = abs(left_distance - right_distance)

                    if j in [i for i in range(seatNum)
                                 if i not in order_seat and
                                    i not in [m + 1 for m in order_seat] and
                                    i not in [n - 1 for n in order_seat]]:
                        # 排除掉所有相邻的座位
                        available_seats.append([j, distance, distance_diff])

            # 按照左右距离和降序，按距离之差的绝对值升序（保证处于中间位置），座位号升序
            available_seats = sorted(available_seats, key=lambda x: (-x[1], x[2], x[0]))
            # 得到索引号最小的座位
            min_seat_index = available_seats[0][0]

            if len(available_seats) == 0:
                return -1
            used_seats[min_seat_index] = True
            order_seat.append(min_seat_index)
        else:
            used_seats[abs(seatOrLeave[i])] = False
            order_seat.remove(abs(seatOrLeave[i]))
        print(order_seat)
    return min_seat_index


if __name__ == '__main__':
    assert solve_method(10, [1, 1, 1, 1, -4, 1]) == 3
```