###This is the Linked List Constructor.
###this will also contain the methods for all linked list operations.
### Class node will be used to create node for all the methords.
### Node class is defined in LLNode file.

from LLNode import Node as Node

class LinkedList:

    def __init__(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        self.length=1

    ##print all items for the list
    def printlist(self):
        start=self.head
        i=0
        while start!=None :
            print(f'Value at::{i}, is::{start.value}')
            start=start.next
            i+=1

    ##add items to the end of the list
    def append(self,value):
        ## handle edge case 1 where there is no items in the list.
        if self.head==None:
            self.head=node
            self.tail=node
            self.length=1
        else: 
            node=Node(value)
            self.tail.next=node
            self.tail=node
        self.length+=1  

    ##pop item at end of the list:method 1 using length of the LL
    ##handle edge case 1 where no items in the list
    ##handle edge case 2 where only 1 item in the list
    def pop(self):

        ###Edge Case 1
        if self.length==1:
            print('warning you are removing only element in the list')
            self.head=None
            self.tail=None
            self.length-=1
        ###Edge Case 2
        elif self.head==None:
            print('No more element in the list, pop is not required.')
        else:
            i=1
            temp=self.head
            while i<self.length-1:
                temp=temp.next
                i+=1
            self.tail=temp
            self.tail.next=None
            self.length-=1

    ##pop item at end of the list:method 1 temp and pre
    ##handle edge case 1 where no items in the list
    ##handle edge case 2 where only 1 item in the list
    def pop_2(self):
        print('----pop_2 starts-----')
        if self.head==None:
            print('Popping operation invalid as the LL is empty')
            return
        if self.head.next==None:
            print('Warning:LL contains only one element, popping it will make it empty')
            self.head.next,self.tail.next=None
            return
        
        temp,pre=self.head,self.head
        while temp.next:
            pre=temp
            temp=temp.next

        pre.next=None    
        self.tail=pre
        self.length-=1
        print(f'Removed {temp.value} from the Linked List')
        print(f'tail is pointing to {self.tail.value} in the Linked List')
        print('----pop_2 ends-----')

    def prepend(self,value):
        print('----prepend starts-----')
        new_node=Node(value)
        if self.length>0:
            new_node.next=self.head
            self.head=new_node
        else:
             self.head=new_node
             self.tail=new_node   

        self.length+=1
        print(f'Added {value} to the begining of the node ')
        print('----prepend ends-----')

    def pop_first(self):
        print('----pop_first starts-----')
        if self.length==0:
            return
        if self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
            return

        self.head=self.head.next
        self.length-=1
        print('----pop_first ends-----')

    ###Index is considered to be the zero based.
    ###If first element is required, pass 0 as the index.
    def get(self,index):
        print('----get starts-----')
        if index >=self.length:
            print(f'index::{index} is greater than length::{self.length}, not returning any element')
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        print('----get ends-----')
        return temp
    
    ###set value replaces the value at given index
    def set_value(self,index,value):
        temp=self.head
        pre=self.head
        for _ in range(index):
            temp=temp.next
        temp.value=value
    
    ###insert node at given index
    def insert(self,index,value):
        print(f'---insert starts at index::{index}----')
        new_node=Node(value)
        temp=self.head
        pre=self.head

        if index==0:
            new_node.next=self.head
            self.head=new_node
            self.length+=1
            return

        for _ in range(index):
            pre=temp
            temp=temp.next

        new_node.next=pre.next
        pre.next=new_node
        self.length+=1

        print(f'---insert ends----')


    ###remove node at given index
    def remove(self,index):
        if self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
            return
        if index==0:
            self.head=self.head.next
            self.length-=1
            return
        pre=self.get(index-1)
        temp=self.get(index) 
        pre.next=temp.next
        temp.next=None
        if pre.next==None:
            self.tail=pre
        self.length-=1

    ###reverse the linked list
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        before=None
        after=temp.next
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after

    ### find middle node using 2 pointers approach
    def find_middle_node(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    
    ### has loop
    def has_loop(self):
        fast=self.head
        slow=self.head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return False
    
    ###kth from end
    def find_kth_from_end(self,k):
        slow=self.head
        fast=self.head
        if self.head is None:
            return None
        for i in range(k-1):
            if fast:
                fast=fast.next
            else :
                return None
        while fast.next:
            slow=slow.next
            fast=fast.next
        return slow
    

    ###partition list
    def partition_list(self,x):
        temp=self.head
        smallerLL=None
        biggerLL=None
        if temp is None:
            return None
        while temp:
            if temp.value<x:
                if smallerLL:
                    smallerLL.append(temp.value)
                else:
                    smallerLL=LinkedList(temp.value)
                    
            else:
                if biggerLL:
                    biggerLL.append(temp.value)
                else:
                    biggerLL=LinkedList(temp.value)
            temp=temp.next
        print(f"before:smaller tail value::{smallerLL.tail.value}")
        print(f"before:bigger tail value::{biggerLL.tail.value}")
        smallerLL.tail.next=biggerLL.head

        print(f"after:smaller tail value::{smallerLL.tail.value}")
        self.head=smallerLL.head
        self.tail=biggerLL.tail
                    
            