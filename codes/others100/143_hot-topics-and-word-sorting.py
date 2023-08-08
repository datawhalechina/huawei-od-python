# encoding: utf-8
"""
@author: Yalin Feng
@file: 143_hot-topics-and-word-sorting.py
@time: 2023/8/8 3:00
@project: huawei-od-python
@desc: 143 查找舆情热调、热词排序
"""
from functools import cmp_to_key
from typing import List
from collections import Counter


def solve_method(topN: int, M: int, data: List[str]) -> str:
    # 单词的加权频数
    freq = {}

    # 单词的标题频数
    word_freq_title = {}

    # 单词在标题中的先后顺序（每个单词记录最小）
    word_appear_title_no = {}

    # 单词在正文中的先后顺序（每个单词记录最小）
    word_appear_content_no = {}

    for i in range(M):
        title, content = data[i * 2].split(), data[i * 2 + 1].split()
        words = set(title).union(content)
        title_counter = Counter(title)
        content_counter = Counter(content)

        for word in words:
            # 统计规则1，计算加权总频数，标题加权系数为3，正文系数为1
            freq[word] = freq.get(word, 0) + title_counter.get(word, 0) * 3
            freq[word] = freq.get(word, 0) + content_counter.get(word, 0)

            # 统计规则2：更新单词的标题频数
            word_freq_title[word] = word_freq_title.get(word, 0) + title_counter.get(word, 0)

            # 统计规则3：单词在标题中的先后顺序（每个单词记录最小
            first_appear_in_title = -1 if word not in title else title.index(word)
            if first_appear_in_title != -1:
                word_appear_title_no[word] = min(first_appear_in_title, word_appear_title_no.get(word, 9999))

            # 统计规则4：单词在正文中的先后顺序（每个单词记录最小
            first_appear_in_content = -1 if word not in content else content.index(word)
            if first_appear_in_content != -1:
                word_appear_content_no[word] = min(first_appear_in_content, word_appear_content_no.get(word, 9999))

    # 定义一个比较函数，用于自定义单词顺序
    def compare_function(word1, word2):
        if word1== word2:
            return 0

        # 规则1: 标题中出现的词语频率系数为3，正文中出现的词语频率系数为1，返回的答案应该按加权频数逆序排列
        condition1 = freq.get(word1) - freq.get(word2)
        if condition1 != 0:
            return -1 * condition1

        # 规则2：当词语出现次数频率相同时，在标题中出现频率次数高的排在前面；（逆序）
        condition2 = word_freq_title.get(word1) - word_freq_title.get(word2)
        if condition2 != 0:
            return -1 * condition2

        # 规则3：如果仍然相同，则按照词语在标题中出现的先后顺序进行排序；（顺序）
        condition3 = word_appear_title_no.get(word1, 9999) - word_appear_title_no.get(word2, 9999)
        if condition3 != 0:
            return condition3

        # 规则4：如果仍相同，则按照词语在正文中出现的先后顺序进行排序，先出现的排在前面。
        condition4 = word_appear_content_no.get(word1, 9999) - word_appear_content_no.get(word2, 9999)
        if condition4 != 0:
            return condition4

    # 使用比较函数
    sorted_words = sorted(freq.keys(), key=cmp_to_key(compare_function))

    result = ' '.join([sorted_words[i] for i in range(topN)])
    return result


if __name__ == '__main__':
    res=solve_method(2, 1, ["Xiangpica shi yige shanxi de cai",
                              "Xiangpica is a dish from Shanxi that is made with flavorful and nutritious ingredients "
                              "such as niacin yeast. Niacin yeast is a type of yeast that is rich in niacin, "
                              "an important nutrient for maintaining a healthy metabolism and producing energy."
                              ])
    print(res)
    assert res=='Xiangpica is'