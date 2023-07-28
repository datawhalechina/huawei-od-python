# 输入获取
issues = input().split(",")
answers = input().split(",")

# 算法入口
def getResult(issues, answers):
    ans = []

    for issue in issues:
        str1 = "".join(sorted(set(issue)))
        find = False

        for answer in answers:
            str2 = "".join(sorted(set(answer)))

            if str1 == str2:
                ans.append(answer)
                find = True
                # break # 如果一个谜面对应多个谜底，这里就不能break，如果一个谜面只对应一个谜底，那这里就要break，考试的时候都试下

        if not find:
            ans.append("not found")

    return ",".join(ans)

# 算法调用
print(getResult(issues, answers))