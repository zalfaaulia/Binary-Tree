# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 23:19:31 2022

@author: Lenovo X380 Yoga
"""

class Node:
  def __init__(self, num):
      self.num = num
      self.right = None
      self.left = None


def countLeaf(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return countLeaf(node.left) + countLeaf(node.right)
 
#just some example
angka = Node(1)

angka.left = Node(7)
angka.right = Node(9)

angka.right.right = Node(9)
angka.left.right = Node(6)
angka.left.left = Node(2)

angka.right.right.left = Node(5)
angka.left.right.right = Node(11)
angka.left.right.left = Node(5)


print("---Node level 1---")
print("Root: ", angka.num)

print()
print("---Node Level 2---")
print("child kiri : ", angka.left.num) 
print("child kanan : ", angka.right.num)

print()
print("---Node level 3----")
print("child dari angka 9 kanan : ", angka.right.right.num)
print("child dari angka 7 kanan : ", angka.left.right.num)
print("child dari angka 7 kiri : ", angka.left.left.num) #2

print()
print("---Node level 4---")
print("child dari angka 9 kiri : ", angka.right.right.left.num)
print("child dari angka 6 kanan : ", angka.left.right.right.num) 
print("child dari angka 6 kiri : ", angka.left.right.left.num)

print()
print("Banyaknya leaf pada binary tree berikut : ", countLeaf(angka))
