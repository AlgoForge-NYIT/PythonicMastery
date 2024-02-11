class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self, value):
        self.root = None if value is None else self.Node(value)

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return self

        def insert_into(node, value):
            if value <= node.value:
                if node.left is None:
                    node.left = self.Node(value)
                else:
                    insert_into(node.left, value)
            else:
                if node.right is None:
                    node.right = self.Node(value)
                else:
                    insert_into(node.right, value)

        insert_into(self.root, value)
        return self

def is_binary_search_tree(node, lower_bound=-float('inf'), upper_bound=float('inf')):
    if not node:
        return True

    # Adjusted to use node.value for compatibility with the BST.Node class
    if node.value <= lower_bound or node.value >= upper_bound:
        return False

    return (is_binary_search_tree(node.left, lower_bound, node.value) and
            is_binary_search_tree(node.right, node.value, upper_bound))

def is_valid_bst(root):
    return is_binary_search_tree(root)

# Test Case 1: Empty Tree
bst1 = BST(None)
print(is_valid_bst(bst1.root))  # Expected Output: True

# Test Case 2: Valid BST
bst2 = BST(4)
bst2.insert(2)
bst2.insert(6)
bst2.insert(1)
bst2.insert(3)
bst2.insert(5)
print(is_valid_bst(bst2.root))  # Expected Output: True

# Test Case 3: Invalid BST
bst3 = BST(5)
bst3.root.left = BST.Node(2)
bst3.root.right = BST.Node(6)
bst3.root.left.right = BST.Node(7)  # This makes it invalid as 7 > 5 but is in left subtree of 5
print(is_valid_bst(bst3.root))  # Expected Output: False
