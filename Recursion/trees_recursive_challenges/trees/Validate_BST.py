from utils.utils import Node, BST

def is_binary_search_tree(node, lower_bound=-float('inf'), upper_bound=float('inf')):
    if not node or node is None:
        return True

    #short circuit
    if node.val <= lower_bound or node.val >= upper_bound:
        return False


    return (is_binary_search_tree(node.left, lower_bound, node.val) and
            is_binary_search_tree(node.right, node.val, upper_bound))

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
# Create a tree structure manually to form an invalid BST
#    5
#   / \
#  2   6
#   \
#    7
bst3 = BST(5)
bst3.root.left = Node(2)
bst3.root.right = Node(6)
bst3.root.left.right = Node(7)  # This makes it invalid as 7 > 5 but is in left subtree of 5
print(is_valid_bst(bst3.root))  # Expected Output: False
