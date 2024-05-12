# @Author

# Gunnidhi Sharma

# nodes which are not leaf node are called non-leaf-nodes.
class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
      
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    def number_of_Non_leaf_node(self,root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        return 1 + self.number_of_Non_leaf_node(root.left) + self.number_of_Non_leaf_node(root.right)
        
    
        
if __name__=="__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)    
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    
    no = tree.number_of_Non_leaf_node(tree.root)
    print(no)
