#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 232_Removing-extra-whitespace.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 232 去除多余空格
"""

def solve_method(text, key_words_idx):
    # 删除需text要处理的多余空格,并记录index
    text_res = ""
    spaces_index = []
    idx = 0
    in_bracket = False
    has_space = False

    # 删除多余空格
    while idx < len(text):
        c = text[idx]
        if c == "'":
            in_bracket = not in_bracket
            text_res += c
            idx += 1
            continue
        
        if in_bracket:
            text_res += c
        else:
            if has_space and c == " ":
                spaces_index.append(idx)
                idx += 1
                continue

            if c == " ":
                has_space = True
            else:
                has_space = False
                
            text_res += c
        idx += 1

    # 根据删除空格的index，计算新的关键词坐标
    for space_idx in spaces_index:
        for idx in key_words_idx:
            if idx > space_idx:
                key_words_idx[key_words_idx.index(idx)] -= 1

    # 返回处理后的文本和关键词坐标
    keyWordsIdxRes = [key_words_idx[i:i + 2] for i in range(0, len(key_words_idx), 2)]
    return text_res, keyWordsIdxRes

def transKeyLocation(keyWordsIdx):
    keyWordsIdx  = keyWordsIdx.split(',')

    res = []
    for idxs in keyWordsIdx:
        res.extend(int(n) for n in idxs.split(' '))
    return res

if __name__ == '__main__':
    text = "Life is painting a  picture, not doing 'a  sum'."
    key_words_idx = "8 15,20 26,43 45"
    key_words_idx = transKeyLocation(key_words_idx)

    text_res = "Life is painting a picture, not doing 'a  sum'."
    key_words_idx_res = [[8, 15], [19, 25], [42, 44]]

    assert solve_method(text, key_words_idx) == (text_res, key_words_idx_res)

    text = "Life is painting a picture, not doing 'a  sum'."
    key_words_idx = "8 15,19 25,42 44"
    key_words_idx = transKeyLocation(key_words_idx)

    text_res = "Life is painting a picture, not doing 'a  sum'."
    key_words_idx_res = [[8, 15], [19, 25], [42, 44]]

    assert solve_method(text, key_words_idx) == (text_res, key_words_idx_res)