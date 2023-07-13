import sys

score =0
#         整数数组 分数 空列表 数组最后的位置
def combine(ints,n,lst,index):
    global score
    # 排除分数小于零且为0时，将0存入对应位置（索引即得分）
    if n <=0:
        # 这里只会执行一次(的吧)，专门处理为0情况的
        if n ==0:
            for i in range(len(lst)):
                ints[lst[i]]=0
            return True
    # 从数组末尾开始往前遍历
    for i in range(index,-1,-1):
        # 非法情况直接跳出循环
        if n <0 or sum(ints)==0:
            break
        x = ints[i]
        if x ==0:
            continue
        lst.append(i)
        # 递归
        if combine(ints,n-x,lst,i-1):
            count = sum(ints)
            if count ==0 or count % score !=0:
                break
            combine(ints,score,[],len(ints)-1)
        lst.pop()
    return sum(ints)==0

if __name__ == "__main__":
    t = int(input())
    p = input().split()
    # 取出整形分数
    ints = [int( p[i] ) for i in range(t)]

    # 计算总分
    count = sum(ints)
    # 排序该数组
    ints.sort()
    # 将最大的单个分数置为下限
    min_score = ints[t -1]

    res =0
    # 从下限到上限遍历所有可能分数
    for i in range(min_score,count //2):
        # 当可以整除时
        if count % i==0:
            score = i
            if combine(ints,score,[],t-1):
                res = score
                break
    print(count if res ==0 else res)