#!/usr/bin/python3

################################################
## module: HuffmanTree.py
## description: A Huffman Tree Class
## YOUR NAME
## YOUR A#
##
## bugs to vladimir dot kulyukin at usu dot edu
################################################

from HuffmanTreeNode import HuffmanTreeNode


class HuffmanTree(object):
    def __init__(self, root=None):
        self.__root = root

    def getRoot(self):
        return self.__root

    def encodeSymbol(self, s):
        if not s in self.__root.getSymbols():
            raise Exception('Unknown symbol')
        else:
            if self.getRoot().getLeftChild():
                if s in self.getRoot().getLeftChild().getSymbols():
                    left = HuffmanTree(self.getRoot().getLeftChild())
                    return '0' + left.encodeSymbol(s)
            if self.getRoot().getRightChild():
                if s in self.getRoot().getRightChild().getSymbols():
                    right = HuffmanTree(self.getRoot().getRightChild())
                    return '1' + right.encodeSymbol(s)
            return ''

    def encodeText(self, txt):
        string = ''
        for char in txt:
            string += self.encodeSymbol(char)
        return string
     
    def decode(self, bin_string):
        decodedlist = ''
        tmpRoot = self.__root

        for char in bin_string:
            if bin_string == '':
                break
            bit = 0
            con = True
            while con:
                if tmpRoot.isLeaf():
                    for s in tmpRoot.getSymbols():
                        decodedlist += s
                    bin_string = bin_string[bit:len(bin_string):]
                    tmpRoot = self.__root
                    con = False
                else:
                    if bin_string[bit] == '0':
                        tmpRoot = tmpRoot.getLeftChild()
                        bit += 1
                    elif bin_string[bit] == '1':
                        tmpRoot = tmpRoot.getRightChild()
                        bit += 1
        return decodedlist
    
    @staticmethod
    def mergeTwoNodes(htn1, htn2):
        symbols = set(htn1.getSymbols())
        for i in htn2.getSymbols():
            symbols.add(i)
        n = HuffmanTreeNode(symbols=symbols, weight=htn1.getWeight() + htn2.getWeight())
        n.setLeftChild(htn1)
        n.setRightChild(htn2)
        return n

    @staticmethod
    def displayHuffmanTreeNode(ht_node, tabs):
        if ht_node is None:
            return
        print(tabs + '{}:{}'.format(ht_node.getSymbols(), ht_node.getWeight()))
        HuffmanTree.displayHuffmanTreeNode(ht_node.getLeftChild(), tabs+'\t')
        HuffmanTree.displayHuffmanTreeNode(ht_node.getRightChild(), tabs+'\t')

    @staticmethod
    def displayHuffmanTree(huff_tree):
        HuffmanTree.displayHuffmanTreeNode(huff_tree.getRoot(), '')

    @staticmethod
    def displayListOfNodes(list_of_nodes):
        for n in list_of_nodes:
            print(str(n))

    @staticmethod
    def fromListOfHuffmanTreeNodes(list_of_nodes, dbg=False):
        if len(list_of_nodes) == 1:
            tree = HuffmanTree(root=list_of_nodes[0])
            return tree
        else:
            weights = []
            for i in range(len(list_of_nodes)):
                weights.append(list_of_nodes[i].getWeight())
            weights.sort()
            w1 = weights[0]
            w2 = weights[1]
            i1 = -1
            i2 = -1
            for i in range(len(list_of_nodes)):
                if list_of_nodes[i].getWeight() == w1:
                    i1 = i
                elif list_of_nodes[i].getWeight() == w2:
                    i2 = i
            if i1 > i2:
                n1 = list_of_nodes.pop(i1)
                n2 = list_of_nodes.pop(i2)
            if i2 > i1:
                n2 = list_of_nodes.pop(i2)
                n1 = list_of_nodes.pop(i1)
            n = HuffmanTree.mergeTwoNodes(n1, n2)
            list_of_nodes.append(n)
            return HuffmanTree.fromListOfHuffmanTreeNodes(list_of_nodes)

    @staticmethod
    def freqMapToListOfHuffmanTreeNodes(freq_map):
        return [HuffmanTreeNode(symbols=set([item[0]]), weight=item[1]) for item in freq_map.items()] 
