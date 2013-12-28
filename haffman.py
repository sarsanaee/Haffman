from Tree_test import Tree_test
from bitstring import BitArray, BitStream
from sys import argv
from Node import Node

class Hafman():
    """This function will do all the progerss you must trace this class to figure out """

    def __init__(self, MyFile):
        self.File = str(open(MyFile, 'r').read())
        self.file_name = MyFile[0:-4]
        self.Data = {}
        self.dataQueue = []
        self.map = {}
        self.coded = ''
        self.currentNode = None

    def repeatFinder(self):
        """ making self.Data for finding the number that each char repeated"""
        for i in self.File:
            if i in self.Data:
                self.Data[i] += 1
            else:
                self.Data[i] = 1

        for i in self.Data.keys():
            self.dataQueue.append((Node((self.Data[i], i))))
        self.dataQueue.sort(key=lambda node: node.getValue()[0])

    def treeMaker(self):
        """As it shows on his face this function makes huffman tree"""

        while len(self.dataQueue) > 1:
            temp1, temp2 = self.dataQueue.pop(0), self.dataQueue.pop(0)  
            self.dataQueue.append(self.nodeJoin(temp1, temp2))  
            self.dataQueue.sort(key=lambda node: node.getValue()[0])
        return self.currentNode

    def nodeJoin(self, right, left):
        '''when we pop two object from queue then we merge them by this function and make new Node'''
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

    def encode(self):
        '''encoding our file'''
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
        with open(self.file_name + '.bin', 'wb') as f:
            b = BitArray(bin=self.coded)
            f.write(b.tobytes())
        #####

    @staticmethod
    def decode(binary_file,map_file):
        '''decoding our file'''
        mapping_dict = eval(open(map_file,"r").read())
        newfile = open('new_decoded_File.txt', 'a')
        tem_map = {}
        for i in range(len(mapping_dict)):
            b = mapping_dict.popitem()
            tem_map[b[1]] = b[0]
        reading_file = open(binary_file,"rb")
        reading_binary = str(BitStream(reading_file.read()).bin)
        code = ''
        for i in reading_binary:
            code = code + i
            if code in tem_map:
                newfile.write(tem_map[code])
                code = '' 
        newfile.close()
        reading_file.close()



def main():
    mode = argv[1]
    if mode == 'e':
        a = Hafman(argv[2])
        a.repeatFinder()
        a.encode()

    elif mode == 'd':    # this is for you to complete   argv[1] = mode     argv[2] = binary file    argv[3] = map file
        Hafman.decode(argv[2],argv[3])
#main()
#a = Hafman('MyFile.txt')
#a.repeatFinder()
#a.encode()
#Hafman.decode('MyFile.bin','MyFile_map.txt')

main()

