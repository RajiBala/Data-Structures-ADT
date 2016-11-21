class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid


def total(tree):
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

def print_tree(tree):
    if tree == None: return
    print tree.cargo,
    print_tree(tree.left)
    print_tree(tree.right)


def print_tree_postorder(tree):
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print tree.cargo
    
def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print tree.cargo,
    print_tree_inorder(tree.right)
    
def print_tree_indented(tree, level=0):
    if tree == None: return
    print_tree_indented(tree.right, level+1)
    print '  ' * level + str(tree.cargo)
    print_tree_indented(tree.left, level+1)

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    else:
        return False

def get_number(token_list):
    x = token_list[0]
    if type(x) != type(0): return None
    del token_list[0]
    return Tree (x, None, None)



def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_number(token_list)
        return Tree ('*', a, b)
    else:
        return a
def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, '+'):
        b = get_sum(token_list)
        return Tree ('+', a, b)
    else:
        return a

def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)         # get the subexpression
        get_token(token_list, ')')      # remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        token_list[0:1] = []
        return Tree (x, None, None)

    
def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)
        if not get_token(token_list, ')'):
            raise 'BadExpressionError', 'missing parenthesis'
        return x
    else:
        # the rest of the function omitted



left = Tree(2)
right = Tree(3)
#binary search tree#

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self,data):
        self.root = None

    

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)
        else:
            print "the tree is empty"

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

# TREEADT1    
# simple binary tree
# in this implementation, a node is inserted between an existing node and the root


class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())



# test tree


myTree = BinaryTree("Maud")
myTree.insertLeft("Bob")
myTree.insertRight("Tony")
myTree.insertRight("Steven")
printTree(myTree)
#TREEADT2

import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def length(self):
        return self.size

    def inorder(self, node):
        if node == None:
            return None
        else:
            self.inorder(node.left)
            print node.key,
            self.inorder(node.right)

    def search(self, k):
        node = self.root
        while node != None:
            if node.key == k:
                return node
            if node.key > k:
                node = node.left
            else:
                node = node.right
        return None

    def minimum(self, node):
        x = None
        while node.left != None:
            x = node.left
            node = node.left
        return x

    def maximum(self, node):
        x = None
        while node.right != None:
            x = node.right
            node = node.right
        return x

    def successor(self, node):
        parent = None
        if node.right != None:
            return self.minimum(node.right)
        parent = node.p
        while parent != None and node == parent.right:
            node = parent
            parent = parent.p
        return parent

    def predecessor(self, node):
        parent = None
        if node.left != None:
            return self.maximum(node.left)
        parent = node.p
        while parent != None and node == parent.left:
            node = parent
            parent = parent.p
        return parent

    def insert(self, k):
        t = TreeNode(k)
        parent = None
        node = self.root
        while node != None:
            parent = node
            if node.key > t.key:
                node = node.left
            else:
                node = node.right
        t.p = parent
        if parent == None:
            self.root = t
        elif t.key < parent.key:
            parent.left = t
        else:
            parent.right = t
        return t


    def delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            succ = self.minimum(node.right)
            if succ.p != node:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.p = succ
            self.transplant(node, succ)
            succ.left = node.left
            succ.left.p = succ

    def transplant(self, node, newnode):
        if node.p == None:
            self.root = newnode
        elif node == node.p.left:
            node.p.left = newnode
        else:
            node.p.right = newnode
        if newnode != None:
            newnode.p = node.p






