class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def addNode(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._addNodeRecursive(self.root, data)

    def _addNodeRecursive(self, node, data):
        if data < node.val:
            if node.left is None:
                node.left = Node(data)
            else:
                self._addNodeRecursive(node.left, data)
        elif data > node.val:
            if node.right is None:
                node.right = Node(data)
            else:
                self._addNodeRecursive(node.right, data)

    def buildTreeFromList(self, datas):
        for data in datas:
            self.addNode(data)

    def search(self, val):
        return self._searchRecursive(self.root, val)

    def _searchRecursive(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._searchRecursive(node.left, val)
        else:
            return self._searchRecursive(node.right, val)

    def preOrder(self):
        result = []
        self._preOrderRecursive(self.root, result)
        return result

    def _preOrderRecursive(self, node, result):
        if node:
            result.append(node.val)
            self._preOrderRecursive(node.left, result)
            self._preOrderRecursive(node.right, result)

    def inOrder(self):
        result = []
        self._inOrderRecursive(self.root, result)
        return result

    def _inOrderRecursive(self, node, result):
        if node:
            self._inOrderRecursive(node.left, result)
            result.append(node.val)
            self._inOrderRecursive(node.right, result)

    def postOrder(self):
        result = []
        self._postOrderRecursive(self.root, result)
        return result

    def _postOrderRecursive(self, node, result):
        if node:
            self._postOrderRecursive(node.left, result)
            self._postOrderRecursive(node.right, result)
            result.append(node.val)

    def getHeight(self):
        return self._getHeightRecursive(self.root)

    def _getHeightRecursive(self, node):
        if node is None:
            return -1
        left_height = self._getHeightRecursive(node.left)
        right_height = self._getHeightRecursive(node.right)
        return 1 + max(left_height, right_height)

    def getSumLeftChild(self, node):
        if node is None or node.left is None:
            return 0
        return self._getSumRecursive(node.left)

    def getSumRightChild(self, node):
        if node is None or node.right is None:
            return 0
        return self._getSumRecursive(node.right)

    def _getSumRecursive(self, node):
        if node is None:
            return 0
        return node.val + self._getSumRecursive(node.left) + self._getSumRecursive(node.right)

    def getTilt(self):
        return self._getTiltRecursive(self.root)

    def _getTiltRecursive(self, node):
        if node is None:
            return 0
        left_sum = self.getSumLeftChild(node)
        right_sum = self.getSumRightChild(node)
        node_tilt = abs(left_sum - right_sum)
        return node_tilt + self._getTiltRecursive(node.left) + self._getTiltRecursive(node.right)


# Code chạy thử
if __name__ == '__main__':
    bst = BinarySearchTree()
    datas = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]

    bst.buildTreeFromList(datas)

    print('Search 7:', bst.search(7))  # False
    print('Search 12:', bst.search(12))  # True

    print('PreOrder:', bst.preOrder())
    print('InOrder:', bst.inOrder())
    print('PostOrder:', bst.postOrder())
    print('Get height:', bst.getHeight())
    print('Sum of left child tree:', bst.getSumLeftChild(bst.getRoot()))
    print('Sum of right child tree:', bst.getSumRightChild(bst.getRoot()))
    print('Tilt of tree:', int(bst.getTilt()))
