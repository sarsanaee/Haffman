class Node:
    """ Famous node class! """
    def __init__(self, root=None):
        self.Root = root
        self.rightChild = None
        self.leftChild = None

    def setRightChild(self, right_val):
        self.rightChild = right_val

    def setLeftChild(self, left_val):
        self.leftChild = left_val

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getValue(self):
        return self.Root
    

