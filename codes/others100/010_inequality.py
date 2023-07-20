# coding:utf-8
from typing import List
def solve_method(line:str)->None:
    # 接受字符串以 “：”分割
    split1 = line.split(";")
    right = True
    error_list:List[int] = []
    # 倒数第一的限制条件
    limits = split1[-1].split(",")
    # 倒数第二的目标值
    aims = split1[-2].split(",")
    # 倒数第三的变量
    vars_=split1[-3].split(",")
    # 限制条件有几个式子就有几个
    for i in range(len(limits)):
        value =0
        # 将目标值转换为浮点
        aim = float(aims[i])
        #系数
        split_=split1[i].split(",")
        for j in range(len(split_)):
            # 系数乘变量
            value += float(split_[j]) * int(vars_[j])
        limit = limits[i]
        # 取绝对差值
        e = int(abs(value - aim))
        # 匹配限制条件
        if limit ==">":
            right = (value > aim) and right
            error_list.append(e)
        elif limit == "<":
            right = (value < aim) and right
            error_list.append(e)
        elif limit ==">=":
            right = (value >= aim)and right
            error_list.append(e)
        elif limit =="<=":
            right = (value <= aim)and right
            error_list.append(e)
        else:
            right = False
    print(right,max(error_list))

line = input()
solve_method(line)