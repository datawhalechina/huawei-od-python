import sys

def solve_method(line:str)->None:
    # 将输入的字符串转换为字符列表 
    chars = list(line)
    # 初始化临时变量为第一个字符
    tmp = chars[0]
    # 初始化位置变量为0
    pos = 0
    for i in range(1,len(chars)):
        # 遍历字符列表中的每个字符
        cur = chars[i]
        # 如果当前字符小于等于临时变量
        if cur <= tmp:
            tmp = cur
            pos = i
    if pos != 0:
        # 将第一个字符放到位置变量所指示的位置
        chars[pos] = chars[0]
        # 将临时变量放到第一个位置
        chars[0] = tmp
    # 将字符列表转换为字符串并输出
    sys.stdout.write("".join(chars))
def main():
    line = input().strip()
    solve_method(line)
if __name__ =="__main__":
    main()