#more info on trees and binary trees in the README file
#implementation of a binary tree with a linked list

#more info on trees and binary trees in the README file
#implementation of a binary tree with a linked list

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.print_tree(start.left, traversal)
            traversal = self.print_tree(start.right, traversal)
        return traversal

if __name__ == '__main__':
  tree = BinaryTree(1)
  tree.root.left = Node(2)
  tree.root.right = Node(3)
  tree.root.left.left = Node(4)
  tree.root.left.right = Node(5)
  print(tree.print_tree(tree.root, "")[:-1])
#result is the tree
