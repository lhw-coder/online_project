
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

# 头插法  链表的数据顺序是逆序的
def creat_linklist(li):
    head = Node(None)
    for val in li:
        p = Node(val)
        p.next = head.next
        head.next = p
    return head

# 尾插法 链表的数据顺序是顺序的
def creat_linklist_tail(li):
    head = Node(Node)
    tail = head
    for val in li:
        p = Node(val)
        tail.next = p
        tail = p



def traverse_linklist(head):
    p = head.next
    while p:
        print(p.data)
        p = p.next

head = creat_linklist([1, 2, 3, 4, 5])
traverse_linklist(head)

# 双链表

class BiNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prior = None

def creat_bilinklist(li):
    head = BiNode(None)
    tail = BiNode(None)
    head.next = tail
    tail.prior = head
    for val in li:
        p = BiNode(val)
        p.next = head.next
        head.next.prior = p
        head.next = p
        p.prior = head

    return head

ll = [1,2,3,"asd"]
print(type(ll))
ll.append("acb")