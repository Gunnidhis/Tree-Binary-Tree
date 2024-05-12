#author

#Gunnidhi Sharrma

#leaf node is a node which has zero child(nodes which are present at lowest level)

class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
      
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    def number_of_Leafnodes(self,root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return self.number_of_Leafnodes(root.left) + self.number_of_Leafnodes(root.right)
        
    
        
if __name__=="__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)    
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    
    no = tree.number_of_Leafnodes(tree.root)
    print(no)
