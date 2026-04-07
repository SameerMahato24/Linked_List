class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        #Empty LinkedList
        self.head = None
        self.n = 0


    #Length of a LinkedLiist
    def __len__(self):
        return self.n
    
    
    #Insertion from head
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n+1


    #Insertion from tail
    def append(self,value):
        if(self.head is None):
            self.head = Node(value)
            self.n += 1
        else:
            current = self.head
            while(current.next!=None):
                current = current.next
            current.next = Node(value)
            self.n = self.n + 1


    #Insert after the given value
    def insert_after(self,after,value):
        new_node = Node(value)
        current = self.head
        while(current!=None):
            if(current.data==after):
                break
            current = current.next
        if(current!=None):
            new_node.next = current.next
            current.next = new_node
            self.n += 1
        else:
            print('Item not found!')

        
    #Insertion at the Kth index
    def insertion(self,index,value):
        if(index==0):
            return self.insert_head(value)
        
        if(index > self.n):
            print("Index out of range.")
            return
        
        if(index == self.n - 1):
            current = self.head
            while(current.next.next != None):
                current = current.next
            current.next = Node(value)
            return
        
        new_node = Node(value)
        current = self.head 
        for i in range(index-1):
            current=current.next
        new_node.next=current.next
        current.next=new_node
        self.n += 1

    def clear(self):
        self.head = None
        self.n = 0


    #Deleting from head
    def delete_head(self):
        if(self.head == None):
            print('Empty LinkedList')
        else:
            self.head = self.head.next
            self.n = self.n-1


    #Deleting from tail
    def pop(self):
        if(self.head == None):
            print('Empty LinkedList')
        current = self.head
        if(current.next == None):
            return self.delete_head()
        while(current.next.next != None):
            current = current.next
        current.next = None
        self.n = self.n-1


    #Deleting inside element
    def remove(self,value):
        if(self.head == None):
            print("Empty LinkedList")

        if(self.head.data==value):
            return self.delete_head()
        
        current = self.head
        while(current.next!=None):
            if(current.next.data==value):
                break
            current = current.next
        if(current.next==None):
            print('Not Found')
        else:
            current.next = current.next.next


    def search(self,item):
        current = self.head
        position = 0
        while(current!=None):
            if(current.data==item):
                print(position)
                break
            current = current.next
            position = position+1
        if(current==None):
            print('Not Found')

    #Fetch data from its index
    def __getitem__(self,index):
        current = self.head
        position = 0
        while(current!=None):
            if(position == index):
                print(current.data)
                break
            current = current.next
            position = position+1
        if(current==None):
            print("Index Error")


    #Traverse
    #str is a special method in python for print func.
    def __str__(self):
        if(self.head == None):
            print("Empty LinkedList")
        result = ""
        current = self.head
        while(current!=None):
            result = result + str(current.data) + "->"
            current=current.next
        return result[:-2]

    
L = LinkedList()
L.append(5)
L.append(2)
L.append(12)
L.append(23)
L.append(11)
print(L)
L.insertion(5,10)
print(L)
L[3]

