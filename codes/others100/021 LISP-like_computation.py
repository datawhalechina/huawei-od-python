#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import floor

def solve(s):
    
    # 分割表达式中的操作符和操作数
    ops = s.split()
    
    stack = list()  # 用于存储操作数和操作符的栈
    res = 0
    
    for ch in ops:
        if ch == "(" or ch.isalpha():
            # 如果是左括号或字母，直接压入栈中
            stack.append(ch)
        elif ch == ")":
            # 如果是右括号，取出栈顶的两个数和操作符进行计算，并将结果压入栈中
            num2 = stack.pop()
            num1 = stack.pop()
            op = stack.pop()
            stack.pop()
            
            if op == "add":
                res = num1 + num2
            elif op == "sub":
                res = num1 - num2
            elif op == "mul":
                res = num1 * num2
            elif op == "div":
                if num2 == 0:
                    # 如果除法操作的除数为0，返回error
                    return "error"
                res = floor(num1 / num2)
            
            # 将计算结果压入栈中
            stack.append(res)
        else:
            # 如果是数字，直接压入栈中
            stack.append(int(ch))

    return stack[0]

if __name__ == "__main__":
    expression = input("请输入表达式，用空格隔开字符: ")
    result = solve(expression)
    print(result)

