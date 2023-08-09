# 096 数大雁

## 题目描述

一群大雁往南飞，给定一个字符串，记录地面上的游客听到的大雁叫声，请给出叫声最少由几只大雁发出。

具体的：
1. 大雁发出的完整叫声为`quack`，因为有多只大雁同一时间嘎嘎作响，所以字符串中可能会混合多个`quack`。
2. 大雁会依次完整发出`quack`，即字符串中`q`、`u`、`a`、`c`、`k`这5个字母，按顺序完整存在才能计数为一只大雁。如果不完整或者没有按顺序则不予计数。
3. 如果字符串不是由`q`、`u`、`a`、`c`、`k`字符组合而成，或者没有找到一只大雁，请返回-1。

## 输入描述

一个字符串，包含大雁`quack`的叫声。字符串长度的取值范围是1 <= 字符串长度 <= 1000，字符串中的字符只有`q`、`u`、`a`、`c`、`k`。

## 输出描述

大雁的数量。

## 示例描述

### 示例一

**输入：**
```text
quackquack
```

**输出：**
```text
1
```

### 示例二

**输入：**
```text
qaauucqcaa
```

**输出：**
```text
-1
```

### 示例三

**输入：**
```text
quacqkuack
```

**输出：**
```text
2
```

## 解题思路

**基本思路：** xxxxx（注：如果存在基本思路，可编写）
1. xxxxx
2. xxxxx
3. xxxxx
4. 返回结果。

## 解题代码