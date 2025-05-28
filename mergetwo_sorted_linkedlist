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
    return head        
    printlinkedlist(head)         
def printdummy(l1,l2):
    dummy=Node(0)
    dummycopy=dummy
    while l1 and l2:
        if l1.val<l2.val:
            dummycopy.next=l1
            l1=l1.next
        else:
            dummycopy.next=l2
            l2=l2.next
        dummycopy=dummycopy.next
    dummycopy.next=l1 if l1 else l2
    return dummy.next
    
def printlinkedlist(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next    

arr=[1,2,3,4,5]
arr1=[1,7,2,9]
arr.sort()
arr1.sort()
l1=linkedlist(arr)
l2=linkedlist(arr1)
m=printdummy(l1,l2)
printlinkedlist(m)


            


