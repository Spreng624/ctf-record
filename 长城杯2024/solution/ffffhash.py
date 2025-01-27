import os
import gmpy2
from Crypto.Util.number import *


class Node:
    def __init__(self, value: int, key: int = None, last=None):
        self.value = value
        self.key = key
        self.last = last


def giao(base_num, i):
    x = 0x0000000001000000000000000000013B
    MOD = 2**128
    base_num = (base_num * x) & (MOD - 1)  # 取后128位
    base_num ^= i
    return base_num


def regiao(base_num, i):
    x = 0xB1041AD2562FF2FF2FF2FF2FF2FF2FF3
    MOD = 2**128
    base_num ^= i
    base_num = (base_num * x) & (MOD - 1)  # 取后128位
    return base_num


def search(tree1: list[list[Node]], tree2: list[list[Node]], tag=True):
    temp = []
    for node1 in tree1[-1]:
        for key in range(16):
            if tag == 1:
                new_node = Node(giao(node1.value, key), key, node1)
            else:
                new_node = Node(regiao(node1.value, key), key, node1)
            # print(hex(new_node.value))
            # 检测是否在tree2中
            for node2 in tree2[-1]:
                if new_node.value == node2.value:
                    return new_node, node2
            temp.append(new_node)
    tree1.append(temp)
    print("treeA:", len(treeA))
    print("treeB:", len(treeB))
    return None, None


def print_tree(tree: list[list[Node]]):
    for i in range(len(tree)):
        print("Level", i, [hex(node.value) for node in tree[i]])


A = 0x6C62272E07BB014262B821756295C58D
B = giao(A, 1)
print(hex(B))
B = giao(B, 2)
print(hex(B))
B = giao(B, 3)
print(hex(B))
B = giao(B, 4)
print(hex(B))

B = 0x978A496D524F0EE5B806E89CF4C1AB48

treeA = [[Node(A)]]
treeB = [[Node(B)]]


node1, node2 = None, None
for i in range(5):
    node1, node2 = search(treeA, treeB, 1)
    if node1:
        break
    node2, node1 = search(treeB, treeA, 0)
    if node1:
        break

if node1:
    path = []
    while node1.last is not None:
        path = [node1.key] + path
        node1 = node1.last
    while node2.last is not None:
        path = path + [node2.key]
        node2 = node2.last
    print(path)

