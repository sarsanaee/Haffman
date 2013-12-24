from Node import Node

class Tree_test(Node):
    '''inja ham fek nakonam moshkeli bashe'''
    def __init__(self,ObjList=[]):
        Node.__init__(self)
        self.objects = ObjList
        self.currentNode  = None
    
    def addNode(self,node_object1):
        self.objects.insert(0, node_object1)
        
    def nodeJoin(self,right,left):
        '''in tabe do ta tuple migire azashoon do ta NODE misaze mizare 
        too objects yani gozashtanesho az tabe bala komak gerefte'''
        self.currentNode = Node((right[0] + left[0],right[1] + left[1] ))
        self.currentNode.setRightChild(Node(right))
        self.currentNode.setLeftChild(Node(left))
        self.addNode(self.currentNode)
        self.currentNode = (right[0] + left[0],right[1] + left[1] )
      


