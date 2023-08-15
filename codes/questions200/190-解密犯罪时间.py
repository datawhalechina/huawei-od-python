def solve_method(time: str) -> str:
    nums = [int(c) for c in time if c !=":"]
    h , m = map(int, time.split(":"))
    lst = []
    for i in nums:
        for j in nums:
            if i <= 5:
                lst.append(i * 10 + j)
    lst.sort()
    for i in lst:
        if i <= m:
            continue
        return format_time(h, i)
    if h != 23:
        for i in lst :
            if i <= h:
                continue
            if i <= 23:
                return format_time(i, lst[0])
    return format_time(lst[0],lst[0])

def format_time(h: int, m: int) -> str:
    return f"{h:02d}:{m:02d}"

if __name__ == "__main__":
    t = input()
    ret = solve_method(t)
    print(ret)