

def reverseWords(line, l, r):
    words = line.strip().split(" ")
    end = len(words) - 1
    if r > end:
        r = end
    if len(words) == 0 or l < 0 or r - l <= 0:
        print('EMPTY')
        return
    while l < r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1
    print(' '.join(words))


if __name__ == '__main__':
    line = input("请输入文章片段：")
    l = input("请输入左边界：")
    r = input("请输入右边界：")
    l, r = int(l), int(r)
    reverseWords(line, l, r)