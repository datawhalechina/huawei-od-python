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
