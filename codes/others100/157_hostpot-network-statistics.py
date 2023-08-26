from collections import Counter

def update_counter(counter, url):
    counter[url] += 1

def get_top_urls(counter, n):
    top_urls = counter.most_common(n)
    sorted_urls = sorted(top_urls, key=lambda x: (-x[1], x[0]))
    return [url for url, count in sorted_urls]

# 初始化计数器
counter = Counter()

while True:
    # 读取输入
    line = input().strip()

    if line.isdigit():
        # 如果是数字，则输出Top N的页面
        n = int(line)
        top_urls = get_top_urls(counter, n)
        for url in top_urls:
            print(url)
    else:
        # 如果是URL，则更新计数器
        update_counter(counter, line)