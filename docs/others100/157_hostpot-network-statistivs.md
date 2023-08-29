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

1. 初始化遇到字符串`N`起始的位置`start_pos`。
2. 初始化计数器`counter`，用于对URL访问次数的统计。
3. 遍历所有的URL：
    - 当遇到数字时，取`[start_pos:i]`这一段的字符串数组，更新计数器。
    - 得到访问次数最高的`N`个页面，并将URL存入结果列表中。
4. 返回结果列表。    

## 解题代码

```python
from collections import Counter


def solve_method(lines):
    result = []
    start_pos = 0
    counter = Counter()
    for i in range(len(lines)):
        if lines[i].isdigit():
            counter.update(lines[start_pos:i])
            top_urls = counter.most_common(int(lines[i]))
            result.append([x[0] for x in top_urls])
            start_pos = i + 1
    return result


if __name__ == '__main__':
    lines = ["news.qq.com", "news.sina.com.cn", "news.qq.com", "news.qq.com",
             "game.163.com", "game.163.com", "www.huawei.com", "www.cctv.com",
             "3", "www.huawei.com", "www.cctv.com", "www.huawei.com",
             "www.cctv.com", "www.huawei.com", "www.cctv.com", "www.huawei.com",
             "www.cctv.com", "www.huawei.com", "3"]
    assert solve_method(lines) == [["news.qq.com", "game.163.com", "news.sina.com.cn"],
                                   ["www.huawei.com", "www.cctv.com", "news.qq.com"]]

    lines = ["news.qq.com", "www.cctv.com", "1",
             "www.huawei.com", "www.huawei.com", "2",
             "3"]
    assert solve_method(lines) == [["news.qq.com"],
                                   ["www.huawei.com", "news.qq.com"],
                                   ["www.huawei.com", "news.qq.com", "www.cctv.com"]]
```

