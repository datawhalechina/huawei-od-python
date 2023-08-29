# 157 热点网络统计

## 题目描述

企业路由器的统计页面，有一个功能，需要动态统计公司访问服多的网页，请设计一个算法，可以高效动态统计`TopN`的页面。

## 输入描述

每一行都是一个URL或一个数字：

- 如果是URL，代表一段时间内的网页访问。 
- 如果是一个数字`N`，代表本次需要输出的`TopN`个URL。 

**输入约束：** 

1. 总访问网页数量小于5000个，单网页访问次数小于65535次。 
2. 网页URL仅由字母数字和：分限符组成且长度小于等于127字节。 
3. 数字是正整数，小于等于10，且小于当前总访问网页数。

## 输出描述

每行输入对应一行输出，输出按访问次数排序的前`N`个URL，用逗号分隔。

**输出要求：**

1. 每次输出要统计之前所有输入，不仅是本次输入。
2. 如果有访问次数相等的URL，按URL的字符串字典序升序排列，输出排序靠前的URL。

## 示例描述

### 示例一

**输入：**

```text
news.qq.com
news.sina.com.cn
news.qq.com
news.qq.com
game.163.com
game.163.com
www.huawei.com
www.cctv.com
3
www.huawei.com
www.cctv.com
www.huawei.com
www.cctv.com
www.huawei.com
www.cctv.com
www.huawei.com
www.cctv.com
www.huawei.com
3
```

**输出：**

```text
news.qq.com,game.163.com,news.sina.com.cn
www.huawei.com,www.cctv.com,news.qq.com
```

### 示例二

**输入：**

```text
news.qq.com
www.cctv.com
1
www.huawei.com
www.huawei.com
2
3
```

**输出：**

```text
news.qq.com
www.huawei.com,news.qq.com
www.huawei.com,news.qq.com,www.cctv.com
```

## 解题思路

使用`Counter`类来实现对`URL`访问次数的统计。在每次输入`URL`时，调用`update_counter`函数更新计数器。在输入数字`N`时，调用`get_top_urls`函数获取访问次数最高的`N`个页面，并按要求进行排序和输出。

## 解题代码

```python
from collections import Counter

def update_counter(counter, url):
    counter[url] += 1

def get_top_urls(counter, n):
    top_urls = counter.most_common(n)
    sorted_urls = sorted(top_urls, key=lambda x: (-x[1], x[0]))
    return [url for url, count in sorted_urls]

# 初始化计数器
counter = Counter()

while True:
    # 读取输入
    line = input().strip()

    if line.isdigit():
        # 如果是数字，则输出Top N的页面
        n = int(line)
        top_urls = get_top_urls(counter, n)
        for i in range(len(top_urls)):
            if i ==len(top_urls)-1:
                print(top_urls[i])
            else:
                print(top_urls[i],end=",")

    else:
        # 如果是URL，则更新计数器
        update_counter(counter, line)def solve_method(lights):
    lights_list = []
    for light in lights:
        id = light[0]
        x1 = light[1]
        y1 = light[2]
        x2 = light[3]
        y2 = light[4]
        # id, x坐标的平均值, y坐标的平均值, 灯高半径
        lights_list.append([id, (x1 + x2) // 2, (y1 + y2) // 2, (y2 - y1) // 2])

    # 将灯按行粗排
    lights_list.sort(key=lambda x: x[2])

    result = []

    # 设置每一行的起始索引
    row_start_index = 0
    # 先使用第1行第1个作为基准灯
    for i in range(1, len(lights_list)):
        # 高低偏差超过灯高度的一半
        if lights_list[i][2] - lights_list[row_start_index][2] > lights_list[row_start_index][3]:
            # 把之前的灯按x坐标排序，并存入结果列表中
            lights_list[row_start_index:i] = sorted(lights_list[row_start_index:i], key=lambda x: x[1])
            result.extend([light[0] for light in lights_list[row_start_index:i]])
            # 记录新一行对应的灯位置
            row_start_index = i

    # 把该行剩余的灯全部加入到结果列表中
    lights_list[row_start_index:] = sorted(lights_list[row_start_index:], key=lambda x: x[1])
    result.extend([light[0] for light in lights_list[row_start_index:]])

    return result
```

