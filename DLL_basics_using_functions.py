class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.n = 0


    def __len__(self):
        return self.n
    
    
    def insert_at_head(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            self.n += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.n += 1


    def append(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            self.n += 1
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.n = self.n + 1


    def insertion(self, index, data):
        if(index == 0):
            return self.insert_at_head(data)
        
        if(index > self.n):
            print("Index out of range.")
            return
        
        if(index == self.n - 1):
            new_node = Node(data)
            current = self.head
            while(current.next.next != None):
                current = current.next
            current.next = new_node
            new_node.prev = current
            return
        
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self.n += 1


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


    def delete_head(self):
        self.head = self.head.next
        self.head.prev = None
        self.n -= 1


    def remove(self, data):
        if(self.head == None):
            print("Empty LinkedList")

        if(self.head.data == data):
            return self.delete_head()
        
        current = self.head
        while(current.next!=None):
            if(current.next.data == data):
                break
            current = current.next
        if(current.next.next==None):
            print('Not Found')
        else:
            current.next = current.next.next
            current.next.prev = current
            

    def pop(self):
        current = self.head
        if(current.next == None):
            return self.delete_head()
        
        while(current.next.next != None):
            current = current.next
        current.next = None
        self.n -= 1


    def clear(self):
        self.head = None
        self.n = 0


    def __str__(self):
        if(self.head == None):
            print("Empty LinkedList")
        result = ""
        current = self.head
        while(current!=None):
            result = result + str(current.data) + "->"
            current=current.next
        return result[:-2]
    
    
L = DoublyLinkedList()
L.append(5)
L.append(2)
L.append(12)
L.append(23)
L.append(11)
print(L)

L.pop()
L.remove(12)
print(L)
