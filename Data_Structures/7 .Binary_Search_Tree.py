class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        return self

    def contains(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            return self.left.contains(value) if self.left else False
        else:
            return self.right.contains(value) if self.right else False

    def traverseDepthFirst_inOrder(self, fn):
        if self.left:
            self.left.traverseDepthFirst_inOrder(fn)
        fn(self)
        if self.right:
            self.right.traverseDepthFirst_inOrder(fn)

    def traverseDepthFirst_preOrder(self, fn):
        fn(self)
        if self.left:
            self.left.traverseDepthFirst_preOrder(fn)
        if self.right:
            self.right.traverseDepthFirst_preOrder(fn)

    def traverseDepthFirst_postOrder(self, fn):
        if self.left:
            self.left.traverseDepthFirst_postOrder(fn)
        if self.right:
            self.right.traverseDepthFirst_postOrder(fn)
        fn(self)

    def traverseBreadthFirst(self, fn):
        queue = [self]
        while queue:
            node = queue.pop(0)
            fn(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def checkIfFull(self):
        result = True
        def check(node):
            nonlocal result
            if node.left and not node.right or not node.left and node.right:
                result = False
        self.traverseBreadthFirst(check)
        return result

    def checkIfBalanced(self):
        heights = []
        def check(node, height):
            if not node.left and not node.right:
                heights.append(height)
                return
            if node.left:
                check(node.left, height + 1)
            if node.right:
                check(node.right, height + 1)
        check(self, 1)
        return max(heights) - min(heights) <= 1


# Test 1: Insertion and In-Order Traversal
bst = BinarySearchTree(10)
bst.insert(5).insert(15).insert(8).insert(3).insert(7).insert(20).insert(17).insert(9).insert(14)
result_inOrder = []
bst.traverseDepthFirst_inOrder(lambda node: result_inOrder.append(node.value))
print("In-Order:", result_inOrder)

# Test 2: CheckIfFull
print("Is Full:", bst.checkIfFull())

# Test 3: CheckIfBalanced
print("Is Balanced:", bst.checkIfBalanced())
