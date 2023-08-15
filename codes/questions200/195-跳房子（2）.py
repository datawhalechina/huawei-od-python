def dfs(nums, remaining, combination, indices, index):
    global minIndexSum, targetCount, result

    if remaining == 0:
        total = 0
        indexSumTemp = 0
        for i in range(3):
            total += combination[i]
            indexSumTemp += indices[i]
        if total == targetCount and indexSumTemp < minIndexSum:
            minIndexSum = indexSumTemp
            result = combination[:]
    else:
        for i in range(index, len(nums)):
            combination.append(nums[i])
            indices.append(i)
            dfs(nums, remaining - 1, combination, indices, i + 1)
            combination.pop()
            indices.pop()


minIndexSum = float('inf')
targetCount = int(input())
nums = list(map(int, input().strip(' [\] ').split(',')))
result = []
dfs(nums, 3, [], [], 0)
output = '[' + ', '.join(map(str, result)) + '] '
print(output)