from Tree_test import Tree_test
from bitstring import BitArray, BitStream
from sys import argv
from Node import Node

class Hafman():
    """khodet ye niga bendaz bebin in tree maker ro mitooni doros koni ya na"""

    def __init__(self, MyFile):
        self.File = str(open(MyFile, 'r').read())
        self.file_name = MyFile[0:-4]
        self.Data = {}
        self.dataQueue = []
        self.map = {}
        self.coded = ''
        self.currentNode = None

    def repeatFinder(self):
        """ in tabe kheili rahate niazi be tozih nadare"""
        for i in self.File:
            if i in self.Data:
                self.Data[i] += 1
            else:
                self.Data[i] = 1

        for i in self.Data.keys():
            self.dataQueue.append((Node((self.Data[i], i))))
        self.dataQueue.sort(key=lambda node: node.getValue()[0])

    def treeMaker(self):
        """in tabe derakhte hafman roo ba komake tavabe class haye digar doros mikone"""

        while len(self.dataQueue) > 1:
            temp1, temp2 = self.dataQueue.pop(0), self.dataQueue.pop(0)  # kharej kardan do onsor az safe olaviat
            #print(temp1.getValue(), temp2.getValue())   # baraye moshahedeye ettefaghat
            self.dataQueue.append(self.nodeJoin(temp1, temp2))  # vared kardan node jadide ijad shode be safe olaviat
            self.dataQueue.sort(key=lambda node: node.getValue()[0])
            print(self.dataQueue)
                # ta in khat bayad derakht ma doros beshe hala dorosto ghalatesho khodet ye niga benadaz
        return self.currentNode

    ###################################
    def nodeJoin(self, right, left):
        if right.getValue()[0] > left.getValue()[0]:
            l = left
            r = right
        else:
            l = right
            r = left
        self.currentNode = Node((right.getValue()[0] + left.getValue()[0], right.getValue()[1] + left.getValue()[1]))
        self.currentNode.setLeftChild(l)
        self.currentNode.setRightChild(r)
        return self.currentNode

    #######################################################
    def encode(self):
        self.map = {}
        tree = self.treeMaker()
        for i in self.Data.keys():
            current = tree
            code = []
            while not (current.getLeftChild() is None and current.getRightChild() is None):
                if i in current.getLeftChild().getValue()[1]:
                    code.append('0')
                    current = current.getLeftChild()
                elif i in current.getRightChild().getValue()[1]:
                    code.append('1')
                    current = current.getRightChild()
            self.map[i] = ''.join(code)
        coded_file = open(self.file_name + '_map.txt', 'w')
        coded_file.write(str(self.map))
        coded_file.close()
        for i in self.File:
            self.coded += self.map[i]
        with open(self.file_name + '.bin', 'wb') as f:                     # write the encoded data to a binary file
            b = BitArray(bin=self.coded)
            f.write(b.tobytes())
        #####


def main():
    mode = argv[1]
    if mode == 'e':
        a = Hafman(argv[2])
        a.repeatFinder()
        a.encode()

    #elif mode == 'd':    # this is for you to complete   argv[1] = mode     argv[2] = binary file    argv[3] = map file

#main()
a = Hafman('MyFile.txt')
a.repeatFinder()
a.encode()


