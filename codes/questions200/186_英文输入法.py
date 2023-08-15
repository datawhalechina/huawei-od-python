import re

def solve_method(s, pre):
    words = re.findall(r'\w+', s)
    word_set = set(words)

    result = []

    for word in word_set:
        if word.startswith(pre):
            result.append(word)
    if not result:
        result.append(pre)

    print(' '.join(sorted(result)))

if __name__ == '__main__':
    s = input()
    pre = input()
    solve_method(s, pre)