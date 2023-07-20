# coding:utf-8

def solve_method(n,jobs):
    # time总时间
    # more超过时间
    time,more = 0, 0
    for i in jobs:
        # 当前工作加上之前的超时时间会超出时间段长度
        if i + more > n:
            # 超出的部分被保存到more中
            more =i+more -n
        else:
            # 当前工作没有超过时间段长度
            more = 0
        # 经历的秒数
        time +=1
    # 下面继续进行循环执行任务
    while more > 0:
        more -n
        time +=1
    print(time)

if __name__ == '__main__':
    n, length = map(int,input().split())
    jobs = list(map(int,input().split()))
    solve_method(n,jobs)




# n = int(input())
# len = int(input())
# l = list(map(int,input().split()))
# time,more=0,0
# for i in l:
#     if i+more > n:
#         more = i+more-n
#     else:
#         more = 0
#     time += 1
# while more > 0:
#     more -= n
#     time += 1
# print(time)