#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 094_sensitive-field-encryption.py
@time: 2023/8/11 17:03
@project: huawei-od-python
@desc: 094 敏感字段加密
"""


def solve_method(k, string):
    commands = []
    command = ""
    # 双引号计数器，用于判断是否在双引号内部
    quote_count = 0
    for ch in string:
        if ch == '"' and quote_count != 1:
            # 遇到第一个双引号
            command += ch
            quote_count += 1
        elif ch == '"' and quote_count == 1:
            # 遇到第二个双引号
            quote_count += 1
            command += ch
            commands.append(command)
            command = ""
        elif ch == '_' and command != "" and quote_count != 1:
            #  遇到下划线，当前命令字不为空，不在双引号内部
            if quote_count == 2:
                quote_count = 0
            commands.append(command)
            command = ""
        elif (command == "" and ch != "_") or ('"' in command) or ch != "_":
            # 遇到非下划线字符，或当前命令字为空且字符不为下划线，或当前命令中包含一个双引号
            command += ch

    if command != "":
        # 将最后一个命令添加到命令列表
        commands.append(command)

    if k < len(commands):
        commands[k] = "******" if '"' not in commands[k] else '"******"'
        return "_".join(commands)
    else:
        return "ERROR"


if __name__ == '__main__':
    assert solve_method(1, "password__a12345678_timeout_100") == "password_******_timeout_100"
    assert solve_method(2, 'aaa_password_"al2_45678"_timeout__100_""_') == 'aaa_password_"******"_timeout_100_""'
