# encoding: utf-8
"""
@author: Yalin Feng
@file: 143_hot-topics-and-word-sorting.py
@time: 2023/8/8 3:00
@project: huawei-od-python
@desc: 143 查找舆情热调、热词排序
"""
import math
from typing import List


def solve_method(topN: int, M: int, articles: List[List[str]]):
    # 构建词语频率字典，key为词语，value是一个4元素列表，每个元素分别表示标题中出现次数、标题位置、正文中出现次数、正文位置。
    word_dict = {}

    for article in articles:
        title, content = article[0], article[1]
        title_words = title.split()
        content_words = content.split()

        for i, word in enumerate(title_words):
            if word not in word_dict.keys():
                word_dict[word] = [1, i, 0, math.inf]
            else:
                word_dict[word][0] += 1

        for i, word in enumerate(content_words):
            if word not in word_dict.keys():
                word_dict[word] = [0, math.inf, 1, i]
            else:
                word_dict[word][2] += 1
                if word_dict[word][3] == -1:
                    word_dict[word][3] = i

    for k, v in word_dict.items():
        title_freq = v[0]
        content_freq = v[2]
        # value为词语出现次数频率、标题中出现次数频率、标题位置、正文位置
        word_dict[k] = [3 * title_freq + content_freq, title_freq, v[1], v[3]]

    # 按照词语出现次数频率从高到低、标题中出现次数频率从高到低、标题位置从前到后、正文位置从前到后排序
    sorted_word_dict = sorted(word_dict.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2], x[1][3]))

    return [x[0] for x in sorted_word_dict[:topN]]


if __name__ == '__main__':
    res = solve_method(2, 1, [["Xiangpica shi yige shanxi de cai",
                               "Xiangpica is a dish from Shanxi that is made with flavorful and nutritious ingredients "
                               "such as niacin yeast. Niacin yeast is a type of yeast that is rich in niacin, "
                               "an important nutrient for maintaining a healthy metabolism and producing energy."
                               ]])
    assert res == ["Xiangpica", "is"]
