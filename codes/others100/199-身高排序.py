h, n = map(int, input().split())
highs = list(map(int, input().split()))
highs.sort(key=lambda x: (abs(x - h), x))
print(' '.join(map(str, highs)))