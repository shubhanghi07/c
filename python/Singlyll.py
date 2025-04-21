class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
        
    def append(self,data):
        if self.last_node is None:
           self.head=Node(data)
           self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
            
    def deleteNode(self,position):
        if self.head is None:
            return
        temp=self.head
        if position==0:
            self.head=temp.next
            temp=None
            return
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return  
        next=temp.next.next
        temp.next=None
        temp.next=next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
    def find_index(self,key):
        current=self.head
        index=0
        while current:
            if current.data==key:
                return index
            current=current.next
            index=index+1
        return-1
a_llist=LinkedList()
for data in[4,-3,1,0,9,11]:
    a_llist.append(data)
print("The Linked List:")
a_llist.display()
print()
print("After deleting an element:")
a_llist.deleteNode(2)
a_llist.display()
print()
key=int(input("What data item would you like to search for?"))
index=a_llist.find_index(key)
if index==-1:
      print(str(key)+"was not found.")
else:
    print(str(key)+"is found at index"+str(index) +'.')
      
          
                             
            
               
