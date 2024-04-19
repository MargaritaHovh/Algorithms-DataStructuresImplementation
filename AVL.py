class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class AVL:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        
        return self._search(node.right, value)
 
    def getMin(self):
        if self.root is None:
            return None
        else:
            return self._getMin(self.root)

    def _getMin(self, node):
        while node and node.left:
            node = node.left
        return node.value
    
    def getMax(self):
        if self.root is None:
            return None
        else:
            return self._getMax(self.root)
        
    def _getMax(self, node):
        while node and node.right:
            node = node.right
        return node.value
    
    def getHeight(self):
        return self._getHeight(self.root)


    def _getHeight(self, node):
        if node is None:
            return -1
        left_height = self._getHeight(node.left)
        right_height = self._getHeight(node.right)
        return max(left_height, right_height) + 1
    

    def getPredecessor(self, value):
        if self.root is None:
            return None
        return self._getPredecessor(self.root, value)

    def _getPredecessor(self, node, value):        
        if node.left:
            return self._getMax(node.left)
        else:
            predecessor = None
            ancestor = self.root
            while ancestor.value != value:
                if ancestor.value < value:
                    predecessor = ancestor.value
                    ancestor = ancestor.right
                else:
                    ancestor = ancestor.left
            return predecessor if predecessor else None

    def getSuccessor(self, value):
        if not self.root:
            return None
        return self._getSuccessor(self.root, value)
    
    def _getSuccessor(self, node, value):
        if node.right:
            return self._getMin(node.right)
        else:
            successor = None
            ancestor = self.root
            while ancestor != node:
                if ancestor.value > node.value:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor.value if successor else None

    def getBalanceFactor(self, node):
        if node is None:
            return 0
        return self._getHeight(node.left) - self._getHeight(node.right)
        

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        if value > node.value:
            node.right = self._insert(node.right, value)

        bf = self.getBalanceFactor(node)

        if bf > 1 and value < node.left.value:
            return self.rightRotate(node)
        if bf > 1 and value > node.left.value:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if bf < -1 and value > node.right.value:
            return self.leftRotate(node)
        if bf < -1 and value < node.right.value:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node
    
    def delete(self, value):
        self.root = self._delete(self.root, value)
    
    def _delete(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            
            node.value = self._getMin(node.right, value)
            node.right = self._delete(node.right, node.value)

        bf = self.getBalanceFactor(node)

        if bf > 1 and self.getBalanceFactor(node.left) >= 0:
            return self.rightRotate(node)
        if bf > 1 and self.getBalanceFactor(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if bf < -1 and self.getBalanceFactor(node.right) <= 0:
            return self.leftRotate(node)
        if bf < -1 and self.getBalanceFactor(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node
    
    
    def rightRotate(self, z):
        x = z.left
        T4 = x.right
        x.right = z
        z.left = T4
        return x
    
    def leftRotate(self, z):
        x = z.right
        T2 = x.left
        x.left = z
        z.right = T2
        return x
    

    def inorderTraversal(self):
        return self._inorderTraversal(self.root)
      
    def _inorderTraversal(self, node):
        if node is not None:
            self._inorderTraversal(node.left)
            print(node.value, end = " ")
            self._inorderTraversal(node.right)
    
    def preorderTraversal(self):
        return self._preorderTraversal(self.root)
      
    def _preorderTraversal(self, node):
        if node is not None:
            print(node.value, end = " ")
            self._preorderTraversal(node.left)
            self._preorderTraversal(node.right)
    
    def postorderTraversal(self):
        return self._postorderTraversal(self.root)
      
    def _postorderTraversal(self, node):
        if node is not None:
            self._postorderTraversal(node.left)
            self._postorderTraversal(node.right)
            print(node.value, end = " ")

    def levelorder(self):
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            result.append(node.value)  

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result




avl = AVL()

avl.insert(20)
avl.insert(1)
avl.insert(15)
avl.insert(10)
avl.insert(5)
avl.insert(2)
avl.insert(4)

print(avl.levelorder())


