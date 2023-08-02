def solve_method(amount, prices):
    prices.sort()
    combinations = []
    dfs(prices, amount, 0, [], combinations)
    return combinations

def dfs(prices, amount, index, combination, combinations):
    # 截止条件1：当前amount等于0，说明已经找到了一组解，将当前解存储在最终列表中，返回
    if amount == 0:
        combinations.append(combination)
        return
    # 截止条件2：最小的面值都大于amount，说明没有解，直接返回
    if index >= len(prices) or prices[index] > amount:
        return
    for i in range(index, len(prices)):
        if(prices[i] <= amount):
            dfs(prices, amount - prices[i], i, combination + [prices[i]], combinations)

if __name__ == "__main__":
    # 500
    # [100, 200, 300, 500]
    amount = int(input().strip())
    prices = list(map(int, input().strip('[').strip(']').split(',')))
    print(solve_method(amount, prices))

    assert sorted(solve_method(500, [100, 200, 300, 500])) == sorted([[100, 100, 100, 100, 100], [100, 100, 100, 200], [100, 100, 300], [100, 200, 200], [200, 300], [500]])
    assert sorted(solve_method(100, [100])) == sorted([[100]])