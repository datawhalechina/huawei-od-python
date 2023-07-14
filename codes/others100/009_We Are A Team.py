# coding:utf-8
import sys
# 读取输入一行并分割转换为整数赋值给n，m
n,m = map(int,sys.stdin.readline().split())
# 关系集合
relationship_sets = []
# 待验证的关系
verify_relationships = []
# 读取m行
for i in range(m):
    relationship = sys.stdin.readline().strip().split()
    # 逐个赋值
    x,y,relation = map(int,relationship)
    # 不等于0证明要验证
    if relation != 0:
        verify_relationships.append(relationship)
    else:
        set_added = False
        for j in range(len(relationship_sets)):
            # 取出关系集合中的每个set
            set_ = relationship_sets[j]
            # 只需要判断其中一个是否在其中
            if x in set_ or y in set_:
                # 加入该集合
                set_.add(x)
                set_.add(y)
                set_added = True
                break
        # 不存在则另外创建新的集合并把xy存入
        if not set_added:
            new_set = set()
            new_set.add(x)
            new_set.add(y)
            relationship_sets.append(new_set)
 # 处理待验证的集合
for i in range(len(verify_relationships)):
    relationship = verify_relationships[i]
    x,y,relation = map(int,relationship)
    if relation != 1:
        print("da pian zi")
        continue
    is_team = False
    for j in range(len(relationship_sets)):
        set_=relationship_sets[j]
        if x in set_ and y in set_:
            print("we are a team")
            is_team = True
            break
    if not is_team:
        print("we are not a team")