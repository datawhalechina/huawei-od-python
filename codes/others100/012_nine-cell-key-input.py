# coding:utf-8
buttonWords = [
    [' '],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', '1'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z']
]

def main():
    # 输入一行字符串
    line = input()
    solveMethod(line)

def solveMethod(line):
    # 表示当前模式（数字模式或字母模式）
    numMode = True
    # 用于构建字符串结果
    builder = ""
    inputs = list(line)
    i = 0
    while i < len(inputs):
        # 获取当前字符
        c = inputs[i]
        if c.isdigit() and c != '0':
            if numMode:
                # 数字则添加到尾部
                builder += c
            else:
                last = c
            count = 0
            while i < len(inputs) and last == inputs[i]:
                last = inputs[i]
                count += 1
                i += 1
            num = int(c)
            buttonWord = buttonWords[num]
            # 偏移量为 (count - 1) % len(buttonWord)，即取余操作，用于循环选择按钮对应的字母
            word = buttonWord[(count - 1) % len(buttonWord)]
            builder += word
            i -= 1
        # 处理切换模式和空格的情况
        if c == '#':
            numMode = not numMode
        elif c == '0':
            builder += '0' if numMode else ' '
        i += 1
        continue
    # 输出构建的字符串结果
    print(builder)

if __name__ == '__main__':
    main()
