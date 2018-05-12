import sys

B = 'Black'
R = 'Red'
class Node:
    def __init__(self, n):
        self.value = n
        self.size = 1
        self.color = R
        self.parent = None
        self.left = None
        self.right = None
    def set_value(self, v):
        self.value = v
    def set_color(self, c):
        self.color = c
    def set_size(self, s):
        if s:
            self.size += 1
        else:
            self.size -= 1
    def set_leaf(self, N):
        self.left = N
        self.right = N
    def is_NIL(self):
        return (self.value is None)
    def get_sibling(self):
        if self.parent.left == self:
            return self.parent.right
        else:
            return self.parent.left
    def get_p2(self):
        if self.parent is None:
            return None
        return self.parent.parent
    def get_ps(self):
        g = self.get_p2()
        if g is None:
            return None
        elif (self.parent == g.left):
            return g.right
        else:
            return g.left

# NIL : leaf node
NIL = Node(None)
NIL.size = 0
NIL.set_color(B)

class OS_tree:
    def __init__(self):
        self.root = NIL

    def get_root(self):
        return self.root

    def set_root(self, node):
        if node.parent is None:
            self.root = node
        else:
            self.set_root(node.parent)

    def find_node(self, node, x, f):  # first, node is root node
        if node.is_NIL():
            return 0
        if f == 'D':
            node.set_size(False)
        if node.value == x:
            return node
        elif node.value > x:
            return self.find_node(node.left, x, f)
        elif node.value < x:
            return self.find_node(node.right, x, f)
    
    def find_loc(self, node, x):  # find node for insert location
        node.set_size(True)
        if node.value == x:
            return 0, "same"
        elif node.value > x:
            if not(node.left.is_NIL()):
                return self.find_loc(node.left, x)
            else:
                return node, "left"
        else:
            if not(node.right.is_NIL()):
                return self.find_loc(node.right, x)
            else:
                return node, "right"

    def rank(self, x):
        node = self.find_node(self.get_root(), x, 'R')
        if node == 0:
            return 0
        else:
            return node.size

    def insert(self, x):
        newNode = Node(x)
        newNode.set_leaf(NIL)
        if self.root.is_NIL():
            self.root = newNode
        else:
            p, d = self.find_loc(self.get_root(), newNode.value)
            if d == "same":
                return p
            elif d == "left":
                p.left = newNode
            else:
                p.right = newNode
            newNode.parent = p
        self.insert_case1(newNode)
        return x

    def insert_case1(self, n):
        if n.parent is None:
            n.set_color(B)
        else:  
            self.insert_case2(n)

    def insert_case2(self, n):
        if n.parent.color != B:
            self.insert_case3(n)

    def insert_case3(self, n):
        u = n.get_ps()
        if not(u is None) and u.color == R:
            n.parent.set_color(B)
            u.set_color(B)
            g = n.get_p2()
            g.set_color(R)
            self.insert_case1(g)
        else:
            self.insert_case4(n)

    def insert_case4(self, n):
        g = n.get_p2()
        if n == n.parent.right and n.parent == g.left:
            self.rotateL(n.parent)
            n = n.left
        elif n == n.parent.left and n.parent == g.right:
            self.rotateR(n.parent)
            n = n.right
        self.insert_case5(n)

    def insert_case5(self, n):
        g = n.get_p2()
        n.parent.set_color(B)
        g.set_color(R)
        if n == n.parent.left:
            self.rotateR(g)
        else:
            self.rotateL(g)

    def rotateL(self, n):
        c = n.right
        p = n.parent
        n_size = n.size
        cl_size = c.left.size
        nl_size = n.left.size
        if not(c.left.is_NIL()):
            c.left.parent = n
        n.right = c.left
        n.parent = c
        c.left = n
        c.parent = p
        if not(p is None):
            if (p.left == n):
                p.left = c
            else:
                p.right = c
        c.size = n_size
        n.size = nl_size + cl_size + 1
        self.set_root(n)

    def rotateR(self, n):
        c = n.left
        p = n.parent
        n_size = n.size
        cr_size = c.right.size
        nr_size = n.right.size
        if not(c.right.is_NIL()):
            c.right.parent = n
        n.left = c.right
        n.parent = c
        c.right = n
        c.parent = p
        if not(p is None):
            if (p.right == n):
                p.right = c
            else:
                p.left = c
        c.size = n_size
        n.size = cr_size + nr_size + 1
        self.set_root(n)

    def delete(self, x):
        n = self.find_node(self.get_root(), x, 'D')
        if n == 0:
            return 0
        if (n.parent is None and n.right.is_NIL() and n.left.is_NIL()):
            self.root = NIL
        else:
            d = self.for_delete(n)
            self.delete_one_child(d)
        return x

    def for_delete(self, node):
        if (node.right.is_NIL() and node.left.is_NIL()):
     	   return node
        if not(node.left.is_NIL()):
            r = node.left
            while not(r.right.is_NIL()):
                r = r.right           
        else:
            r = node.right
        node.value, r.value = r.value, node.value
        return r

    def replace(self, n, c):    
        if n.parent.left == n:
            n.parent.left = c
        else:
            n.parent.right = c
        if not(c.is_NIL()):
            c.parent = n.parent

    def delete_one_child(self, n):
        c = n.left if n.right.is_NIL() else n.right
        self.replace(n, c)
        if n.color == B:
            if c.color == R:
                c.set_color(B)
            else:
                self.delete_case1(c)

    def delete_case1(self, n):
        if n.parent != None:
            self.delete_case2(n)

    def delete_case2(self, n):
        s = n.get_sibling()
        if s.color == R:
            n.parent.set_color(R)
            s.set_color(B)
            if n == n.parent.left:
                self.rotateL(n.parent)
            else:
                self.rotateR(n.parent)
        self.delete_case3(n)

    def delete_case3(self, n):
        s = n.get_sibling() 
        if ((n.parent.color == B) and
            (s.color == B) and
            (s.left.color == B) and
            (s.right.color == B)):
            s.set_color(R)
            self.delete_case1(n.parent)
        else:
            self.delete_case4(n)

    def delete_case4(self, n):
        s = n.get_sibling()
        if ((n.parent.color == R) and
            (s.color == B) and
            (s.left.color == B) and
            (s.right.color == B)):
            s.set_color(R)
            n.parent.set_color(B)
        else:
            delete_case5(n)

    def delete_case5(self, n):
        s = n.get_sibling()
        if (s.color == B):
            if ((n == n.parent.left) and
                (s.right.color == B) and
                (s.left.color == R)):
                s.set_color(R)
                s.left.set_color(B)
                self.rotateR(s)
            elif ((n==n.parent.right) and
                    (s.left.color == B) and
                    (s.right.color == R)):
                s.set_color(R)
                s.right.set_color(B)
                self.rotateL(s)
        self.delete_case6(n)
    
    def delete_case6(self, n):
        s = n.get_sibling()
        s.set_color(n.parent.color)
        n.parent.set_color(B)
        if n == n.parent.left:
            s.right.set_color(B)
            self.rotateL(n.parent)
        else:
            s.left.set_color(B)
            self.rotateR(n.parent)






    def print_tree(self, node, blank):
        if not(node.is_NIL()):
            print("|", blank + str(node.value))
            self.print_tree(node.left, blank + " ")
            self.print_tree(node.right, blank + " ")
