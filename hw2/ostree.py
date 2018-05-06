NIL = False
B = 'Black'
R = 'Red'
class Node:
   def __init__(self, n):
      self.value = n
      self.size = 1
      self.color = R
      self.parent = NIL
      self.left = NIL
      self.right = NIL
   def set_color(self, c):
      self.color = c
   def set_parent(self, p):
      self.parent = p
   def set_left(self, n):
      self.left = n
   def set_right(self, n):
      self.right = n
   def set_size(self, s):
      self.size = s
   def get_sibling(self):
      if self.parent.left == self:
         return self.parent.right
      else:
         return self.parent.left
   def get_p2(self):
      return self.parent.parent
   def get_ps(self):
      g = self.get_p2()
      if not(g):
         return NIL
      elif (self.parent == g.left):
         return g.right
      else:
         return g.left

class OS_tree:
   def __init__(self):
      self.root = NIL

   def find_node(self, node, x):  # first, node is root node
      if node == NIL:
         return False
      elif node.value == x:
         return node
      elif node.value < x:
         return self.find_node(node.left, x)
      elif node.value > x:
         return self.find_node(node.right, x)
      else:
         print("Error : Find node")
   
   def find_loc(self, node, x):  # find node for insert location
      if node.value > x:
         if not(node.left):
            return find_loc(node.left, x)
         else:
            return node, "left"
      else:
         if not(node.right):
            return find_loc(node.right, x)
         else:
            return node, "right"


   def insert(self, x):
      newNode = Node(x)
      if not(self.root):
         self.root = newNode
      else:
         p, d = find_loc(newNode)
         if d == "left":
            p.left = newNode
         else:
            p.right = newNode
         newNode.parent = p
      insert_case1(newNode)

   def insert_case1(self, n):
      if not(n.parent):
         newNode.set_color(B)
      else:
         insert_case2(n)

   def insert_case2(self, n):
      if n.parent.color != B:
         insert_case3(n)

   def insert_case3(self, n):
      u = n.get_ps(n)
      if u!=NIL and u.color == R:
         n.parent.set_color(B)
         u.set_color(B)
         g = n.get_p2()
         g.set_color(R)
         insert_case1(g)
      else:
         insert_case4(n)

   def insert_case4(self, n):
      g = n.get_p2()

      if n == n.parent.right and n.parent == g.left:
         rotateL(n.parent)
         n = n.left
      elif n = n.parent.left and n.parent == g.right:
         rotateR(n.parent)
         n = n.right
      insert_case5(n)

   def insert_case5(self, n):
      g = n.get_p2()
      n.parent.set_color(B)
      g.set_color(R)
      if n == n.parent.left:
         rotateR(g)
      else:
         rotateL(g)

   def rotateL(self, n):
      c = n.right
      p = n.parent

      if (c.left != NIL):
         c.left.parent = n
      n.right = c.left
      n.parent = c
      c.left = n
      c.parent = parent

      if (p != NIL):
         if (p.left == n):
            p.left = c
         else:
            p.right = c

   def rotateR(self, n):
      c = n.left
      p = n.parent

      if (c.right != NIL):
         c.right.parent = n
      n.left = c.right
      n.parent = c
      c.right = n
      c.parent = parent

      if (p != NIL):
         if (p.right == n):
            p.right = c
         else:
            p.left = c
   def replace(n, c):
      if n.parent.left == n:
         n.parent.left = c
      else:
         n.parent.right = c
      if not(c):
         c.parent = n.parent
         return c
      else:
         return c

   def delete_one_child(self, n):
      c = n.left if not(n.right) else n.right
      is_NIL = replace(n, c)
      if not(is_NIL) and n.color==B:
         if c.color == R:
            c.set_color = B
         else:
            delete_case1(c)

   def delete_case1(self, n):
      if n.parent != NIL:
         delete_case2(n)

   # def delete_case2(self, n):
   #    s = n.get_sibling()
   #    if 




         
      