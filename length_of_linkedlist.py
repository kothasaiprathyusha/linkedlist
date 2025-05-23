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
        count=0
        temp=head
        while(temp):
            count+=1
           
            temp=temp.next
        print(count)    

arr=list(map(int,input().split()))
linkedlist(arr)

            


