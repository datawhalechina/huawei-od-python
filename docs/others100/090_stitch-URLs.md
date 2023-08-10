# 090 拼接URL

## 题目描述

给定一个URL前缀和URL后缀，通过`,`分隔，需要将其连接为一个完整的URL，如果前缀结尾和后缀开头都没有`/`，需要自动补上`/`连接符，如果前缀结尾和后缀开头都为`/`，需要自动去重。

约束：不用考虑前后缀URL不合法情况。

## 输入描述

URL前缀（一个长度小于100的字符串）

URL后缀（一个长度小于100的字符串）

## 输出描述

拼接后的URL

## 示例描述

### 示例一

**输入：**
```text
/acm,/bb
```

**输出：**
```text
/acm/bb
```

### 示例二

**输入：**
```text
/abc/,/bcd
```

**输出：**
```text
/abc/bcd
```

### 示例三

**输入：**
```text
/acd,bef
```

**输出：**
```text
/acd/bef
```

### 示例四

**输入：**
```text
,
```

**输出：**
```text
/
```

## 解题思路

1. 对字符串进行`,`分隔，得到字符串列表`urls`。
2. 将字符串列表中的每一个元素去掉首尾的`/`，然后再用`/`进行拼接。
3. 如果仅为单个`/`，则返回，否则，需要在头部添加一个`/`。
4. 返回结果。

## 解题代码

```python
def solve_method(urls):
    urls = urls.split(",")
    if len(urls) == 0:
        return "/"

    urls = "/".join([x.strip("/") for x in urls])
    result = urls if urls == "/" else "/" + urls
    return result


if __name__ == '__main__':
    assert solve_method("/acm,/bb") == "/acm/bb"
    assert solve_method("/abc/,/bcd") == "/abc/bcd"
    assert solve_method("/acd,bef") == "/acd/bef"
    assert solve_method(",") == "/"
```