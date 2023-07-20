def wordsChain(words, k):
    builder = words[k]
    del words[k]
    words = sorted(words, key=lambda x: (-len(x), x))
    flag, index = True, 0
    while words and index < len(words):
        if words[index].startswith(builder[-1]):
            builder += words[index]
            del words[index]
            index = 0
        else:
            index += 1
    return builder


if __name__ == '__main__':
    k = int(input("请输入起始单词索引："))
    N = int(input("请输单词数组长度："))
    words = []
    for _ in range(N):
        words.append(input().strip())
    res = wordsChain(words, k)
    print(res)
