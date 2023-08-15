import sys


def solve_method(line, start, end):
    words = line.strip().split()
    start = max(start, 0)
    end = min(end, len(words) - 1)

    if end == start or start > len(words) - 1 or end < 0:
        print("EMPTY")
    else:
        list = words[:start]
        for i in range(end, start - 1, -1):
            list.append(words[i])
        list += words[end + 1:]

        res = "".join(list)
        print(res)


if __name__ == "__main__":
    line = input().strip()
    start, end = map(int, input().strip().split())
    solve_method(line, start, end)