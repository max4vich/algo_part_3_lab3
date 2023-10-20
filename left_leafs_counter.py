class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    return calculateBranchSums(root, False)


def calculateBranchSums(node, isLeft):
    if node is None:
        return 0

    if node.left is None and node.right is None and isLeft:
        return node.value

    leftSum = calculateBranchSums(node.left, True)
    rightSum = calculateBranchSums(node.right, False)

    return leftSum + rightSum


if __name__ == "__main__":
    root = BinaryTree(12)
    root.left = BinaryTree(10)
    root.right = BinaryTree(14)
    root.right.left = BinaryTree(13)
    root.right.right = BinaryTree(15)
    root.left.right = BinaryTree(11)
    root.left.left = BinaryTree(9)
    root.left.left.left = BinaryTree(8)
    print(branchSums(root))
