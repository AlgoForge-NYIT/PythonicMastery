from utils.utils import Node, BST

def check_height(root):

    if root is None:
        return 0

    left_height = check_height(root.left)
    if left_height == -1:
        return -1

    right_height = check_height(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    # checking heights of each subtree
    result = max(left_height, right_height) + 1
    return result

def check_bst(bst):
    return check_height(bst) != -1


# Test Case 1: Empty Tree
bst1 = BST(None)
print(check_bst(bst1.root))  # Expected Output: True

# Test Case 2: Balanced Tree
bst2 = BST(4)
bst2.insert(2)
bst2.insert(6)
bst2.insert(1)
bst2.insert(3)
bst2.insert(5)
print(check_bst(bst2.root))  # Expected Output: True


# Test Case 3: Unbalanced Tree
bst3 = BST(1)
bst3.insert(2)
bst3.insert(3)
bst3.insert(4)
bst3.insert(5)
print(check_bst(bst3.root))  # Expected Output: False
