class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def display(self):
        if self.isempty()==True:
            print('None')
        else:
            temp = self.head
            while temp!=None:
                print(temp.data,end="  ")
                temp = temp.next
            
def reverse(root):

    if root is None or root.next is None:
        return root
        
    rest = reverse(root.next)

    root.next.next = root
    root.next = None

    return rest