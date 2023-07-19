# coding:utf-8
import collections
def solve_method(ints):
    # 用来存储每个数字的频率
    map = collections.defaultdict(int)
    for pair in ints:
        for i in range(pair[0],pair[1] + 1):
            map[i] += 1
    # 创建一个由元组组成的列表，每个元组包含一个数字和它的频率
    list = [(k,v) for k,v in map.items()]
    # 根据数字的频率对列表进行降序排序
    list.sort(key=lambda x:x[1],reverse=True)
    print(list[0][0])

if __name__ =="__main__":
    n = int(input().strip())
    ints = [list(map(int,input().strip().split())) for _ in range(n)]
    solve_method(ints)