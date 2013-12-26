from Node import Node


class Tree_test(Node):
    """inja ham fek nakonam moshkeli bashe"""

    def __init__(self):
        Node.__init__(self)
        self.temp = []
        self.currentNode = None


    def nodeJoin(self, right, left):
        """in tabe do ta tuple migire azashoon do ta NODE misaze mizare
        too objects yani gozashtanesho az tabe bala komak gerefte"""


        if self.currentNode is None:
            self.currentNode = Node((right[0] + left[0], right[1] + left[1]))
            self.currentNode.setRightChild(Node(right))
            self.currentNode.setLeftChild(Node(left))
        else:
            self.temp.append(self.currentNode)
            self.currentNode = Node((right[0] + left[0], right[1] + left[1]))
            if len(self.temp) == 2:
                if (self.temp[0].getValue() == right and self.temp[1].getValue() == left) or (self.temp[0].getValue() == left and self.temp[1].getValue() == right):
                    self.currentNode.setRightChild(self.temp[0])
                    self.currentNode.setLeftChild(self.temp[1])
                    self.temp.clear()
            for i in self.temp:
                if i.getValue() == right:
                    self.currentNode.setRightChild(i)
                    self.currentNode.setLeftChild(Node(left))
                    self.temp.remove(i)
                elif i.getValue() == left:
                    self.currentNode.setRightChild(Node(right))
                    self.currentNode.setLeftChild(i)
                    self.temp.remove(i)
                else:
                    self.currentNode.setRightChild(Node(right))
                    self.currentNode.setLeftChild(Node(left))
        #else
        #    self.currentNode.setRightChild(Node(right))
        #    self.currentNode.setLeftChild(temp)