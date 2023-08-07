# 034 删除指定目录

## 题目描述

某文件系统中有 N 个目录，每个目录都一个独一无二的 D。每个目录只有一个付目录
但每个目录下可以有零个或多个子目录，目录结构呈树状结构。
假设 根目录的 ID 为`0`，且根目录没有父目录，ID 用唯一的正整数表示，并统一编号
现给定目录 ID 和其付目录 ID 的对应父子关系表，`[子目录ID,父目录ID]`，以及一个待删除的目录 ID.
请计算并返回一个 ID 序列，
表示因为删除指定目录后剩下的所有目录，
返回的 ID 序列以递增序输出

注意：1. 被删除的目录或文件编号一定在输入的 D 序列中;2.当一个目录删除时，它所有的子目录都会被删除

## 输入描述

输入的第一行为父子关系表的长度 `m`; 接下来的 `m` 行为 `m` 个父子关系对最后一行为待删除的 ID。序列中的元素以空格分割，
参见样例。

## 输出描述

输出一个序列，表示因为删除指定目录后，剩余的目录 ID。

## 示例描述

### 示例一

**输入：**

```Plain Text
5
8 6
10 8
6 0
20 8
2 6
8
```

**输出：**

```Plain Text
2 6
```

## 解题思路

**基本思路：** 参考[华为OD机试 - 删除指定目录（Python）](https://blog.csdn.net/qq_39132095/article/details/129156104?ops_request_misc=&request_id=711cdcbd477b40189386135499ee0f89&biz_id=&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~koosearch~default-5-129156104-null-null.268^v1^control&utm_term=%E5%88%A0%E9%99%A4%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E8%BE%93%E5%87%BA%E5%88%A0%E9%99%A4%E5%90%8E%E6%9C%80%E5%A4%A7&spm=1018.2226.3001.4450)

1. 输入的第一行是整数 n，表示节点的个数。接下来的 n 行每行2个数，表示节点编号和其节点编号。最后一行为要删除的节点编号 rmld。

2. 将每个节点存储在一个列表 nodes 中，将每个节点的父节点存储在另一个列表 parents 中。

3. build_tree 函数使用节点和父节点构建树。遍历节点列表，如果节点不在树中，则将其添加到树中，并将其父节点存储为它的子节点；否则，将其添加为现有节点的子节点。如果节点的父节点是 0，则跳过。

4. m_node()函数递归地从树中删除一个节点。如果节点没有子节点，则从树中直接删除。否则，递归删除它的子节点，并将它从树中删除。最后，输出剩余节点的编号。

## 解题代码

```Python
tree = {}


def build_tree(parent, node):
    for i in range(len(node)):
        node_key = node[i]
        parent_key = parent[i]
        if node_key not in tree:
            tree[node_key] = []
        if parent_key == 0:
            continue
        parent_list = None
        if parent_key in tree:
            parent_list = tree[parent_key]
        else:
            parent_list = []
            tree[parent_key] = parent_list
        parent_list.append(node_key)


def rm_node(node):
    children = tree.get(node)
    if children is None:
        return
    if len(children) == 0:
        tree.pop(node, None)
        return
    for child in children:
        rm_node(child)
    tree.pop(node, None)


if __name__ == '__main__':
    num = int(input())
    nodes = []
    parents = []
    for i in range(num):
        line = input().split()
        nodes.append(int(line[0]))
        parents.append(int(line[1]))
    rmId = int(input())
    build_tree(parents, nodes)
    rm_node(rmId)
    for e in tree.keys():
        print(e, end=' ')
    print()
```



