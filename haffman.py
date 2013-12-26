from Tree_test import Tree_test
from queue import PriorityQueue
from bitstring import BitArray, BitStream
from sys import argv

class Hafman(Tree_test):
    """khodet ye niga bendaz bebin in tree maker ro mitooni doros koni ya na"""

    def __init__(self, MyFile):
        Tree_test.__init__(self)
        self.File = str(open(MyFile, 'r').read())
        self.file_name = MyFile[0:-4]
        self.Data = {}
        self.dataQueue = PriorityQueue()
        self.map = {}
        self.coded = ''

    def repeatFinder(self):
        """ in tabe kheili rahate niazi be tozih nadare"""
        for i in self.File:
            if i in self.Data:
                self.Data[i] += 1
            else:
                self.Data[i] = 1

        for i in self.Data.keys():
            self.dataQueue.put((self.Data[i], i))

    def treeMaker(self):
        """in tabe derakhte hafman roo ba komake tavabe class haye digar doros mikone"""

        code_segment = ''  # felan ziad mohem nis male oon paeine ke comment shode

        while not self.dataQueue.empty():
            temp1, temp2 = self.dataQueue.get(), self.dataQueue.get()  # kharej kardan do onsor az safe olaviat
            print(temp1, temp2)   # baraye moshahedeye ettefaghat
            self.nodeJoin(temp1, temp2)  # in tabe vasl konnandeye NODE ha be ham hast ke too Tree_test tarif shode
            if not self.dataQueue.empty():
                self.dataQueue.put(self.currentNode.getValue())  # vared kardan node jadide ijad shode be safe olaviat
                # ta in khat bayad derakht ma doros beshe hala dorosto ghalatesho khodet ye niga benadaz
        return self.currentNode

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
        coded_file = open(self.file_name+'_map.txt', 'w')
        coded_file.write(str(self.map))
        coded_file.close()
        for i in self.File:
            self.coded += self.map[i]
        with open(self.file_name + '.bin', 'wb') as f:                     # write the encoded data to a binary file
            b = BitArray(bin=self.coded)
            f.write(b.tobytes())

def main():
    mode = argv[1]
    if mode == 'e':
        a = Hafman(argv[2])
        a.repeatFinder()
        a.encode()

    #elif mode == 'd':    # this is for you to complete   argv[1] = mode     argv[2] = binary file    argv[3] = map file

main()


