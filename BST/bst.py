import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key):
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.val = key  # Value of the node


class BinarySearchTree:
    def __init__(self):
        self.root = None  # The root of the BST

    def insert(self, root, key):
        # Recursive function to insert a node with given key in BST
        if root is None:
            return Node(key)  # Creating a new node if root is empty
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)  # Insert in right subtree
            else:
                root.left = self.insert(root.left, key)  # Insert in left subtree
        return root

    def inorder_traverse(self, root, values=[]):
        # Function for inorder traversal of the BST
        if root:
            self.inorder_traverse(root.left, values)  # Traverse left subtree
            values.append(root.val)  # Visit node
            self.inorder_traverse(root.right, values)  # Traverse right subtree
        return values

    def search(self, root, key):
        # Function to search a given key in BST
        if root is None or root.val == key:
            return root  # Return node if found
        if root.val < key:
            return self.search(root.right, key)  # Search in right subtree
        return self.search(root.left, key)  # Search in left subtree

    def delete_node(self, root, key):
        # Function to delete a node with given key from BST
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete_node(root.left, key)  # Delete from left subtree
        if key > root.val:
            root.right = self.delete_node(root.right, key)  # Delete from right subtree
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root.right = None
                return temp
            elif root.right is None:
                temp = root.left
                root.left = None
                return temp
            # Node with two children
            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp)
        return root

    def min_value_node(self, node):
        # Function to find the node with the minimum value in BST
        current = node
        while current.left is not None:
            current = current.left
        return current


def plot_tree(tree, parent_name, graph, pos=None, level=0,
              width=2., vert_gap=0.2, xcenter=0.5):
    if pos is None:
        pos = {parent_name: (xcenter, 1 - level * vert_gap)}
    else:
        pos[parent_name] = (xcenter, 1 - level * vert_gap)
    neighbors = list(graph.neighbors(parent_name))
    if len(neighbors) != 0:
        dx = width / 2
        nextx = xcenter - width / 2 - dx / 2
        for neighbor in neighbors:
            nextx += dx
            pos = plot_tree(tree, neighbor, graph=graph, pos=pos,
                            level=level + 1, width=dx, xcenter=nextx)
    return pos


def create_graph_and_plot(tree, root):
    graph = nx.DiGraph()

    def build_graph(node, parent=None):
        if node:
            graph.add_node(node.val)
            if parent:
                graph.add_edge(parent.val, node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

    build_graph(root)

    pos = plot_tree(tree, root.val, graph=graph)
    nx.draw(graph, pos, with_labels=True, arrows=False, node_size=3000, node_color="skyblue")


bst_a = BinarySearchTree()
list_a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]

bst_b = BinarySearchTree()
list_b = [149, 38, 65, 197, 60, 176, 13, 217, 5, 11]

bst_c = BinarySearchTree()
list_c = [49, 38, 65, 97, 64, 76, 13, 77, 5, 1, 55, 50, 24]

for item in list_a:
    bst_a.root = bst_a.insert(bst_a.root, item)

for item in list_b:
    bst_b.root = bst_b.insert(bst_b.root, item)

for item in list_c:
    bst_c.root = bst_c.insert(bst_c.root, item)

plt.figure(figsize=(12, 8))
create_graph_and_plot(bst_a, bst_a.root)
plt.title('Binary Search Tree Visualization')
plt.show()

plt.figure(figsize=(12, 8))
create_graph_and_plot(bst_b, bst_b.root)
plt.title('Binary Search Tree Visualization')
plt.show()

plt.figure(figsize=(12, 8))
create_graph_and_plot(bst_c, bst_c.root)
plt.title('Binary Search Tree Visualization')
plt.show()

