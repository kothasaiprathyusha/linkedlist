class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
def linkedlist(arr):
    head=None
    for data in arr:
        if head==None:
            head=Node(data)
            temp=head
        else:
            temp.next=Node(data)
            temp=temp.next 
    printlinkedlist(head)          
def printlinkedlist(head):
        temp=head
        while(temp):
            print(temp.val)
            temp=temp.next

arr=list(map(int,input().split()))
linkedlist(arr)

            

