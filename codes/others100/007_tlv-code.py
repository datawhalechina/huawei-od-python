# coding:utf-8

# def solveMethod(tag:str,source:str)->None:
#     p=0
#     # 迭代扫描
#     while p < len (source):
#         # 取字符串的0~1位置上的
#         curTag = source[p:p + 2]
#         # 因为是小端序所以要逆过来拼接
#         lenHEX = source[p + 6:p + 8] + source[p + 3:p + 5]
#         # 转换为十进制
#         lenDEC = int(lenHEX,16)
#         # 判断匹配tag
#         if tag == curTag:
#             # 取出往后lenDEC个位置的字符
#             value = source[p +9: p +9 + lenDEC * 3]
#             print(value)
#         p += 9 + lenDEC * 3

# if __name__ == '__main__':
#     tag = input()
#     source = input()
#     solveMethod(tag,source)

# 改进版
def solveMethod(tag:str,source:str)->None:
    p=0
    # 迭代扫描
    while p < len (source):
        # 取字符串的0~1位置上的
        curTag = source[p]
        # 因为是小端序所以要逆过来拼接
        lenHEX = source[p+2] + source[p+1]
        # 转换为十进制
        lenDEC = int(lenHEX,16)
        # 判断匹配tag
        if tag == curTag:
            # 取出往后lenDEC个位置的字符
            value = source[p +3: p +3 + lenDEC]
            print(' '.join(value))
        p += 3 + lenDEC

if __name__ == '__main__':
    tag = input()
    source = input().split(" ")
    solveMethod(tag,source)