class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None
    
    def getMin(self):
        if not self.root:
            return None
        else:
            return self._getMin(self.root)

    def _getMin(self, node):
        if node.left is None:
            return node.value
        return self._getMin(node.left)

    def getMax(self):
        if not self.root:
            return None
        else:
            return self._getMax(self.root)
        
    def _getMax(self, node):
        if node.right is None:
            return node.value
        return self._getMax(node.right)
    
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
            while ancestor != node:
                if ancestor.value < node.value:
                    predecessor = ancestor
                    ancestor = ancestor.right
                else:
                    ancestor = ancestor.left
            return predecessor.value if predecessor else None

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
        
    def insert(self, value):
        self.root = self._insert(self.root, value)
    
    def _insert(self, node, value):   # Inserts a unique value into the BST
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
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
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            
            node.value = self._getMin(node.right)
            node.right = self._delete(node.right, node.value)

        return node

    def inorder_iterative(self):
        result = []
        stack = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result

    def preorder_iterative(self):
        result = []
        stack = []
        current = self.root

        while current or stack:
            if current:
                result.append(current.value)
                stack.append(current.right)
                current = current.left           
            else:
                current = stack.pop()

        return result

    def postorder_iterative(self):
        if not self.root:
            return []
        
        stack1 = [self.root]
        stack2 = []
        result = []

        while stack1:
            node  = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            result.append(node.value)

        return result


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
    


bst = BinarySearchTree()

bst.insert(50)
bst.insert(20)
bst.insert(60)

print("Search for 20:", bst.search(20))  
print("Search for 45:", bst.search(45))  

print("Minimum value:", bst.getMin())    
print("Maximum value:", bst.getMax())    
print("Height of the BST:", bst.getHeight()) 

print("Predecessor of 50:", bst.getPredecessor(50))  
# print("Successor of 50:", bst.getSuccessor(50))     

# print("Inorder traversal:", bst.inorder_iterative())    
# print("Preorder traversal:", bst.preorder_iterative())   
# print("Postorder traversal:", bst.postorder_iterative()) 

# print("Level-order traversal:", bst.levelorder())    


