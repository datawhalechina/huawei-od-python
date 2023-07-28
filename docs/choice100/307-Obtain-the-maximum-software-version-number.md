# 307 获取最大软件版本号

## 题目描述
Maven版本号定义，<主版本>.<次版本>.<增量版本>-<里程碑版本> \
举例3.1.4-beta 其中，主版本和次版本都是必须的，主版本，次版本，增量版本由多位数字组成，可能包含前导零，里程碑版本由字符串组成。 \
<主版本>.<次版本>.<增量版本>：基于数字比较 \
里程碑版本：基于字符串比较,采用字典序 \
比较版本号时，按从左到右的顺序依次比较。基于数字比较， 只需比较忽略任何前导零后的整数值 。
输入2个版本号，输出最大版本号
## 输入描述
输入2个版本号，换行分割，每个版本的最大长度小于50  
主版本，次版本，增量版本：基于字符串比较,比如 `1.5 > 1.4 > 1.3.11 > 1.3.9`  
里程碑版本：基于字符串比较 比如 `1.2-beta-3 > 1.2-beta-11`
## 输出描述
版本号相同时输出第一个输入版本号

### 示例一
**输入：**
```shell
2.5.1-C
1.4.2-D
```

**输出：**
```shell
2.5.1-C
```

**说明：**  
主版本，数字2大于1


### 示例二
**输入：**
```shell
1.3.11-S2
1.3.11-S13
```

**输出：**
```shell
1.3.11-S2
```

**说明：**  
里程碑版本，S2大于S13

### 示例三
**输入：**
```shell
1.05.1
1.5.01
```

**输出：**
```shell
1.05.1
```

**说明：**  
版本号相同，输出第一个版本号

### 示例四
**输入：**
```shell
1.5
1.5.0
```

**输出：**
```shell
1.5.0
```

**说明：**  
主次相同，存在增量版本大于不存在

### 示例五
**输入：**
```shell
1.5.1-A
1.5.1-a
```

**输出：**
```shell
1.5.1-a
```

**说明：**  
里程碑版本号，字符串比较a大于A

## 解题思路
1. 将两个版本号 version_a 和 version_b 按照点号进行分割，得到各个部分。
2. 对于主次版本的前两个部分，逐个比较它们的大小。如果有任何一个部分不相等，就返回较大的版本号.
3. 如果两个版本号的部分数量都大于2，说明它们可能有增量版本和里程碑版本。
- 1. 将增量版本部分按破折号  进行分割，得到各个部分
- 2. 比较增量版本的第一个部分的大小。如果不相等，返回较大的版本号
- 3. 如果增量版本部分有两个部分(含里程碑版本)，比较里程碑版本的大小。如果有任何一个版本的里程碑版本较大，就返回较大
的版本号。
- 4. 如果增量版本部分没有里程碑版本，比较增量版本部分的大小。如果其中一个版本的增量版本部分长度较长，就返回较大的版本
4. 如果上述条件都不满足，说明其中一个版本的部分数量较少，直接比较主次版本的部分数量。返回部分数量较多的版本号.

## 解题代码

```python
import re
 
# 输入获取
v1 = input()
v2 = input()
 
 
# 算法入口
def getResult(v1, v2):
    pattern = r"^(\d+)(?:\.(\d+))(?:\.(\d+))?(?:\-(.+))?$"
 
    major1, minor1, patch1, mile1 = re.findall(pattern, v1)[0]
    major2, minor2, patch2, mile2 = re.findall(pattern, v2)[0]
 
    if major1 != major2:
        if int(major1) > int(major2):
            return v1
        else:
            return v2
 
    if int(minor1) != int(minor2):
        if int(minor1) > int(minor2):
            return v1
        else:
            return v2
 
    if patch1 != patch2:
        if patch1 != "" and patch2 != "":
            if int(patch1) > int(patch2):
                return v1
            elif int(patch1) < int(patch2):
                return v2
        elif patch1 != "" and patch2 == "":
            return v1
        elif patch1 == "" and patch2 != "":
            return v2
 
    if mile1 != mile2:
        if mile1 != "" and mile2 != "":
            if mile1 > mile2:
                return v1
            elif mile1 < mile2:
                return v2
        elif mile1 != "" and mile2 == "":
            return v1
        elif mile1 == "" and mile2 != "":
            return v2
 
    return v1
 
 
# 算法调用
print(getResult(v1, v2))
```