class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preOrder(self,root):
        if root == None:
            return 
        
        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
        
        
    def inOrder(self,root):
        if root == None:
            return
        
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)
        
        
    def postOrder(self,root):
        if root == None:
            return 
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" ")
        
    
        
if __name__=="__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)    
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    
    tree.inOrder(tree.root)
    print("\n")    
    tree.preOrder(tree.root)
    print("\n")
    tree.postOrder(tree.root)
    
    
