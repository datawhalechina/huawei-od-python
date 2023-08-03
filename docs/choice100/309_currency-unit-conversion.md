# 309 货币单位换算

## 题目描述

记账本上记录了若干条多国货币金额，需要转换成人民币分（fen），汇总后输出。每行记录一条金额，金额带有货币单位，格式为数字+单位，可能是单独元，或者单独分，或者元与分的组合。

要求将这些货币全部换算成人民币分（fen）后进行汇总，汇总结果仅保留整数，小数部分舍弃。

元和分的换算关系都是1:100，如下：  
> 1CNY=100fen（1元=100分）  
1HKD=100cents（1港元=100港分）  
1JPY=100sen（1日元=100仙）  
1EUR=100eurocents（1欧元=100欧分）  
1GBP=100pence（1英镑=100便士）  

汇率如下表
| CNY | JPY | HKD | EUR | GBP |
|-|-|-|-|-|
| 100 | 1825 | 123 | 14 | 12 |

即 100CNY = 1825JPY = 123HKD = 14EUR = 12GBP

## 输入描述

第一行输入为`N`，`N`表示记录数，取值范围是0 < N < 100。

之后`N`行，每行表示一条货币记录，且该行只会是一种货币。

## 输出描述

将每行货币转换成人民币分（`fen`）后汇总求和，只保留整数部分。输出格式只有整数数字，不带小数，不带单位。

## 示例描述

### 示例一
**输入：**
```text
1
100CNY
```

**输出：**
```text
10000
```

**说明：**  
`100CNY`转换后是`10000fen`，所以输出结果为10000。

### 示例二
**输入：**
```text
1
3000fen
```

**输出：**
```text
3000
```

**说明：**  
`3000fen`，结果就是3000。

### 示例三

**输入：**
```text
1
123HKD
```

**输出：**
```text
10000
```
**说明：**

HKD与CNY的汇率关系是123:100，所以换算后，输出结果为10000。

### 示例四

**输入：**
```text
2
20CNY53fen
53HKD87cents
```

**输出：**
```text
6432
```

**说明：**  

20元53分+53港元87港分，换算成人民币分后汇总为6432。

## 解题思路

1. 根据题意，写出各个货币变换成`fen`的转换值。
2. 使用正则表达式获取货币数量和货币单位。
3. 使用`zip`遍历货币数量和货币单位：
   - 将货币数量乘以转换值，可得到`fen`的总额。
   - 将总额进行累加，存入结果值。
4. 返回结果值。    

## 解题代码

```python
import re


def solve_method(amounts):
    exchange = {
        "CNY": 100,
        "JPY": 100 / 1825 * 100,
        "HKD": 100 / 123 * 100,
        "EUR": 100 / 14 * 100,
        "GBP": 100 / 12 * 100,
        "fen": 1,
        "cents": 100 / 123,
        "sen": 100 / 1825,
        "eurocents": 100 / 14,
        "pence": 100 / 12
    }

    ans = 0

    s = "".join(amounts)
    nums = re.findall(r"\d+", s)
    units = re.findall(r"[a-zA-Z]+", s)
    for num, unit in zip(nums, units):
        ans += int(num) * exchange[unit]

    return int(ans)


if __name__ == '__main__':
    amounts = ["100CNY"]
    assert solve_method(amounts) == 10000
    amounts = ["3000fen"]
    assert solve_method(amounts) == 3000
    amounts = ["123HKD"]
    assert solve_method(amounts) == 10000
    amounts = ["20CNY53fen", "53HKD87cents"]
    assert solve_method(amounts) == 6432
```