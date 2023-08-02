# 305 网上商城优惠活动（一）

## 题目描述

**背景**

某网上商城举办优惠活动，发布了满减、打折、无门槛3种优惠券，分别为：

1. 每满100元优惠10元，无使用数限制，如100~199元可以使用1张减10元，200~299可使用2张减20元，以此类推；
2. 92折券，1次限使用1张，如100元，则优惠后为92元；
3. 无门槛5元优惠券，无使用数限制，直接减5元。

**优惠券使用限制：**

每次最多使用2种优惠券，2种优惠可以叠加（优惠叠加时以优惠后的价格计算），以购物200元为例，可以先用92折券优惠到184元，再用1张满减券优惠10元，最终价格是174元，也可以用满减券2张优惠20元为180元，再使用92折券优惠到165（165.6向下取整）元，不同使用顺序的优惠价格不同，以最优惠价格为准。

在一次购物中，同一类型优惠券使用多张时必须一次性使用，不能分多次拆开穿插使用（不允许先使用1张满减券，再用打折券，再使用1张满减券）。

**问题：**

请设计实现一种解决方法，帮助购物者以最少的优惠券获得最优的优惠价格。优惠后价格越低越好，同等优惠价格，使用的优惠券越少越好，可以允许某次购物不使用优惠券。

**约定：**

优惠活动每人只能参加一次，每个人的优惠券种类和数量是一样的。

## 输入描述

第一行：每个人拥有的优惠券数量（数量取值范围为[0, 10]），按满减、打折、无门槛的顺序输入。
第二行：表示购物的人数`n`（1 <= n <= 10000）。

最后`n`行：每一行表示某个人优惠前的购物总价格（价格取值范围(0, 1000]，都为整数）。

约定：输入都是符合题目设定的要求的。

**备注：**

1. 优惠券数量都为整数，取值范围为[0, 10]。
2. 购物人数为整数，取值范围为[1, 10000]。
3. 优惠券的购物总价为整数，取值范围为(0, 1000]。
4. 优惠后价格如果是小数，则向下取整，输出都为整数。

## 输出描述

每行输出每个人每次购物优惠后的最低价格以及使用的优惠券总数量，每行的输出顺序和输入的顺序保持一致。

## 示例描述

### 示例一
**输入：**

```text
3 2 5
3
100
200
400
```

**输出：**
```text
65 6
155 7
338 4
```

**说明：**  

输入说明：
- 第一行：3种优惠券数量分别为满减券3张，打折券2张，无门槛5张。
- 第二行：总共3个人购物。
- 第三行：第一个人购物优惠前价格为100元。
- 第四行：第二个人购物优惠前价格为200元。
- 第五行：第三个人购物优惠前价格为400元。

输出说明：

输入3个人，输出3行结果，同输入的顺序，对应每个人的优惠结果，如下：
- 第一行：先使用1张满减券优惠到90元，再使用5张无门槛券优惠25元，最终价格是65元，总共使用6张优惠券。
- 第二行：先使用2张满减券优惠到180元，再使用5张无门槛券优惠25元，最终价格是155元，总共使用7张优惠券。
- 第三行：先使用1张92折券优惠到368元，再使用3张满减券优惠30元，最终价格是338元，总共使用4张优惠券。


## 解题思路

1. 构建三个函数，分别表示满减策略`full_discount`、打折策略`discount`、无门槛策略`threshold_free`。
2. 根据无门槛策略和打折策略，可得到以下公式：
$$
\begin{aligned}   
& x - 5 \leqslant 0.92x \\
\Rightarrow & 0.08x \leqslant 5 \\
\Rightarrow & x \leqslant 62.5
\end{aligned}
$$
3. 遍历所有用户的购物价格：
   - 当购物价格小于等于62元时，使用无门槛券，再使用打折券。
   - 当购物价格大于62元小于100元时，使用打折券，再使用无门槛券。
   - 比较使用满减券和打折券的优惠价格：
        - 如果满减券更优惠，对比使用无门槛券和打折券。
        - 如果打折券更优惠，对比使用无门槛券和满减券。
   - 计算优惠价格和使用券的数量。 
4. 返回每个用户的优惠价格和使用券的数量。

## 解题代码

```python
def full_discount(res, ticket):
    """
    满减规则
    :param res: 总价
    :param ticket: 满减券数量
    :return: 总价满减后结果，对应数组含义是 (用券后剩余总价， 使用满减券数量)
    """
    # 满100最多用1张满减券，满200最多用2张满减券....
    # price总价最多使用price/100张券
    use_tickets = 0
    max_count = int(res / 100)
    # 实际可使用的满减券数量
    count = min(ticket, max_count)

    res -= count * 10
    ticket -= count
    use_tickets += count
    return res, use_tickets


def discount(res, ticket):
    """
    打折规则
    :param res: 总价
    :param ticket: 打折券数量
    :return: 总价打折后结果，对应数组含义是 (用券后剩余总价， 使用打折券数量)
    """
    use_tickets = 0
    if ticket > 0:
        res = int(res * 0.92)
        use_tickets += 1
    return res, use_tickets


def threshold_free(res, ticket):
    """
    无门槛规则
    :param res: 总价
    :param ticket: 无门槛券数量
    :return: 门槛券用后结果，对应数组含义是 (用券后剩余总价， 使用无门槛券数量)
    """
    use_tickets = 0
    while res > 0 and ticket > 0:
        res -= 5
        # 避免无门槛券过多会导致优惠后总价小于0
        res = max(res, 0)
        ticket -= 1
        use_tickets += 1
    return res, use_tickets


def solve_method(t1, t2, t3, prices):
    """
    :param t1: 满减的优惠券
    :param t2: 打折的优惠券
    :param t3: 无门槛的优惠券
    :param prices: 用户的购物价格
    :return:
    """
    result = []
    for price in prices:
        res_t1, tickets_t1 = full_discount(price, t1)
        res_t2, tickets_t2 = discount(price, t2)
        res_t3, tickets_t3 = threshold_free(price, t3)
        tickets_res = 0
        if price < 100:
            if price <= 62 and t3 > 0:
                # 先使用无门槛券，再使用打折券
                res, tickets_res = discount(res_t3, t2)
                tickets_res += tickets_t3
            else:
                # 先使用打折券，再使用无门槛券
                res, tickets_res = threshold_free(res_t2, t3)
                tickets_res += tickets_t2

            result.append([res, tickets_res])
            continue

        if res_t1 < res_t2:
            copy_res = res_t1
            tickets_res += tickets_t1
            # 先使用满减券，再使用无门槛券
            r3, tickets_r3 = threshold_free(res_t1, t3)
            # 或者先使用满减券，再使用打折券
            r2, tickets_r2 = discount(copy_res, t2)
            if r3 < r2:
                res = r3
                tickets_res += tickets_r3
            else:
                res = r2
                tickets_res += tickets_r2
        else:
            copy_res = res_t2
            tickets_res += tickets_t2
            # 先使用打折券，再使用无门槛券
            r3, tickets_r3 = threshold_free(res_t2, t3)
            # 或者使用打折券，再使用满减券
            r1, tickets_r1 = full_discount(copy_res, t1)
            if r3 < r1:
                res = r3
                tickets_res += tickets_r3
            else:
                res = r1
                tickets_res += tickets_r1

        result.append([res, tickets_res])

    return result
```