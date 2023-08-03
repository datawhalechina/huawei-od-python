#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

