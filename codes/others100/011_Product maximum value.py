# coding:utf-8
line = input().strip()
split = line.split(',')

max_val =0
for i in range(len(split)):
    for j in range(i,len(split)):
        chars = list(split[j])
        k = 0
        while k < len(chars):
            if split[i].find(chars[k]) != -1:
                break
            k += 1
        tmp = len(split[i]) * len(split[j])
        if k == len(chars) and tmp > max_val:
            max_val = tmp
print(max_val)