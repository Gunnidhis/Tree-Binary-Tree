# @author
#Gunnidhi Sharma

# Full node is a node which has stictly 2 child 

#full node is a node which has two nodes 

class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
      
class BinaryTree:
    
    def __init__(self):
        self.root = None
    
    def number_of_fullNodes(self,root):
        if root == None:
            return 0
        if root.left == None and root.left == None:
            return 0
        return self.number_of_fullNodes(root.left) + self.number_of_fullNodes(root.right) + (1 if root.left != None and root.right != None else 0)
        
    
        
if __name__=="__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)    
    tree.root.left.right = Node(5)
    # tree.root.right.left = Node(6)
    # tree.root.right.right = Node(7)
    
    no = tree.number_of_fullNodes(tree.root)
    print(no)
