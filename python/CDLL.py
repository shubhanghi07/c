class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insertEnd(value):
    global start
    if (start==None):
        new_node=Node(0)
        new_node.data=value
        new_node.next=new_node.prev=new_node
        start=new_node
        return
    last=(start).prev
    new_node=Node(0)
    new_node.data=value
    new_node.next=start
    (start).prev=new_node
    new_node.prev=last
    last.next=new_node
def insertBegin(value):
    global start
    last=(start).prev
    new_node=Node(0)
    new_node.data=value
    new_node.next=start
    new_node.prev=last
    last.next=(start).prev=new_node
    start=new_node
def display():
    global start
    temp=start
    print("traversal in forword direction")
    while (temp.next!=start):
         print(temp.data,end=" ")
         temp=temp.next
    print(temp.data)
if __name__=='__main__':
    global start
    start=None
    insertEnd(5)
    insertBegin(4)
    insertEnd(7)
    insertEnd(8)
    print("created circuler DLL")
    display()
        
        
        
        
