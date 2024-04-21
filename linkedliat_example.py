class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def get_length(self):
        current=self.head
        length=0
        while current is not None:
            length +=1
            current=current.next
        #print(length)
        return length
    def get_middle(self):
        slow_node=self.head
        fast_node=self.head
        while fast_node is not None and fast_node.next is not None:
            slow_node=slow_node.next
            fast_node=fast_node.next.next
        #print(slow_node.data)
        return slow_node
    def delete_value(self,value):
        current=self.head
        prev=None
        while current is not None:
            if current == value:
                if prev is not None:
                    prev.next=current.next
                else :
                    self.head=current.next
            else :
                prev=current
                current=current.next
    def printf(self):
        current=self.head
        print('@',current.data)
        while current is not None:
            print(current.data)
            current=current.next
    def insert_at_end(self,value):
        new=Node(value)
        if self.head is None:
            self.head=new
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new
    def insert_at_beginning(self,value):
        new=Node(value)
        if self.head is None:
            self.head=new
            return 
        new.next=self.head
        self.head=new



new=Node(10)
linked_list=DoublyLinkedList()
new.next=linked_list.head
linked_list.head=new
linked_list.head.next=Node(20)
#linked_list.delete_value(20)
linked_list.get_length()
linked_list.get_middle()
linked_list.insert_at_end(30)
linked_list.insert_at_beginning(1)
linked_list.printf()

