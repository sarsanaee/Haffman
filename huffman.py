from bitstring import BitArray, BitStream
from sys import argv
from Node import Node
from tarfile import *
from os import remove


class Huffman():
    """huffman compression main class"""

    def __init__(self, my_file):
        self.file = str(open(my_file, 'r').read())
        self.file_name = my_file[0:-4]
        self.data = {}
        self.data_queue = []
        self.map = {}
        self.coded = ''
        self.current_node = None

    def repeat_finder(self):
        """ making self.Data for finding out the occurrences of each char"""
        for i in self.file:
            if i in self.data:
                self.data[i] += 1
            else:
                self.data[i] = 1

        for i in self.data.keys():
            self.data_queue.append((Node((self.data[i], i))))
        self.data_queue.sort(key=lambda node: node.getValue()[0])

    def tree_maker(self):
        """As it shows on his face this function which makes Huffman tree"""

        while len(self.data_queue) > 1:
            temp1, temp2 = self.data_queue.pop(0), self.data_queue.pop(0)
            self.data_queue.append(self.node_join(temp1, temp2))
            self.data_queue.sort(key=lambda node: node.getValue()[0])
        return self.current_node

    def node_join(self, right, left):
        """when we pop two object from queue then we merge them by this function and make new Node"""
        if right.getValue()[0] > left.getValue()[0]:
            l = left
            r = right
        else:
            l = right
            r = left
        self.current_node = Node((right.getValue()[0] + left.getValue()[0], right.getValue()[1] + left.getValue()[1]))
        self.current_node.setLeftChild(l)
        self.current_node.setRightChild(r)
        return self.current_node

    def encode(self):
        """encoding our file"""
        self.map = {}
        tree = self.tree_maker()
        for i in self.data.keys():
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
        coded_file = open('map.txt', 'w')
        coded_file.write(str(self.map))
        coded_file.close()
        for i in self.file:
            self.coded += self.map[i]
        with open('file.bin', 'wb') as f:
            b = BitArray(bin=self.coded)
            f.write(b.tobytes())

    @staticmethod
    def decode():
        """decoding our file"""
        mapping_dict = eval(open('map.txt', "r").read())
        newfile = open('new_file' + '.txt', 'a')
        tem_map = {}
        for i in range(len(mapping_dict)):
            b = mapping_dict.popitem()
            tem_map[b[1]] = b[0]
        reading_file = open('file.bin', "rb")
        reading_binary = str(BitStream(reading_file.read()).bin)
        code = ''
        for i in reading_binary:
            code += i
            if code in tem_map:
                newfile.write(tem_map[code])
                code = ''
        newfile.close()
        reading_file.close()

    def to_tar(self):
        x = TarFile.open(self.file_name + '.tar', 'w')
        x.add("file.bin")
        x.add("map.txt")

    @staticmethod
    def extract_tar(name):
        x = TarFile.open(name, 'r')
        x.extractall()


def main():
    mode = argv[1]
    if mode == 'e':                      # argv[1] = mode     argv[2] = txt file
        a = Huffman(argv[2])
        a.repeat_finder()
        a.encode()
        a.to_tar()
        remove("file.bin")
        remove("map.txt")

    elif mode == 'd':                      # argv[1] = mode     argv[2] = tar file
        Huffman.extract_tar(argv[2])
        Huffman.decode()
        remove("file.bin")
        remove("map.txt")

    else:
        print("Invalid option\n", "Usage:\n", "python3 Huffman.py e [your text file]              for encrypting\n",
              "python3 Huffman.py d [your Huffman tar file]       for decrypting\n", )

main()

