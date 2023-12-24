class Node:
def __init__(self, data):
self.data = data
self.left = self.right = None
def insert(root, data):
if root is None:
return Node(data)
if data < root.data:
root.left = insert(root.left, data)
elif data > root.data:
root.right = insert(root.right, data)
return root
def print_inorder(node):
if node is not None:
print_inorder(node.left)
print(node.data, end=" ")
print_inorder(node.right)
def print_preorder(node):
if node is not None:
print(node.data, end=" ")
print_preorder(node.left)
print_preorder(node.right)
def print_postorder(node):
if node is not None:
print_postorder(node.left)
print_postorder(node.right)
print(node.data, end=" ")
root = None
root = insert(root, 8)
root = insert(root, 16)
root = insert(root, 24)
root = insert(root, 2)
root = insert(root, 14)
root = insert(root, 6)
root = insert(root, 9)
print("Inorder traversal:")
print_inorder(root)
print("\n")
print("Preorder traversal:")
print_preorder(root)
print("\n")
print("Postorder traversal:")
print_postorder(root)
print("\n")
