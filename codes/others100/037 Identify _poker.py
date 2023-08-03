#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 同花
def check_tonghua(colors):
    # 判断花色是否一致
    return len(set(colors)) == 1

# 顺子
def check_shunzi(cards, nums):
    if ("".join(nums) == "2345A"):
        return True
    # 检查是否构成顺子
    for i in range(1, len(nums)):
        if (cards[nums[i - 1]] + 1 != cards[nums[i]]):
            return False
 
    return True
 

 
# 四条
def check_four(nums):
    num_count = {}

    # 统计牌的数量
    for num in nums:
        if num in card_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # 检查是否存在四张相同牌值的牌
    values = list(num_count.values())
    return len(values) == 2 and 4 in values

  
 
# 葫芦
def check_hulu(nums):
    num_count = {}

    # 统计牌的数量
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # 检查是否存在三张相同牌值的牌和两张相同牌值的牌
    values = list(num_count.values())
    return len(values) == 2 and (2 in values or 3 in values)
  
 
 
# 三条
def check_three(nums):
    num_count = {}
    # 统计牌的数量
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    # 判断是否有三张相同牌值得牌
    return any(count == 3 for count in num_count.values())


def main(nums,colors):
    cards ={"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 11,"Q": 12,"K": 13,"A": 14}
    nums = sorted(nums, key=lambda x: cards[str(x)])
    if (check_shunzi(cards, nums) and check_tonghua(colors)):
        return 1
    elif (check_sitiao(nums)):
        return 2
    elif (check_hulu(nums)):
        return 3
    elif (check_tonghua(colors)):
        return 4
    elif (check_shunzi(cards, nums)):
        return 5
    elif (check_three(nums)):
        return 6
    else:
        return 0
 
if __name__ == "__main__":
    nums = []
    colors = []
    while True:
        poker = [x for x in input().split(" ")]
        if len(poker) >= 2:
            nums.append(poker[0])
            colors.append(poker[1])
        else:
            # 用户输入为空，跳出循环
            break

    res = main(nums,colors)
    print(res)

