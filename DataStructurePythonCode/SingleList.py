""" Implement a single list data structure.

    2018.02.03
    Jie
"""

class Node(object):
    def __init__(self, val, p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0
        self.tail = 0

    def __getitem__(self, item):
        if self.is_empty():
            print('linklist is empty.')
            return
        elif item < 0 or item > self.getlength():
            print('The given key is error.')
            return
        else:
            return self.getItem(item)

    def __setitem__(self, key, value):
        if self.is_empty():
            print('linklist is empty.')
            return
        elif key < 0 or key > self.getlength():
            print('The given key is error.')
            return
        else:
            self.delete(key)
            return self.insert(key)

    def initList(self, data):
        self.head = Node(data[0])
        self.tail = Node(data[-1])

        p = self.head

        for i in data[1:-1]:
            node = Node(i)
            p.next = node
            p = p.next

        p.next = self.tail

    def getLength(self):
        p = self.head
        length = 0
        while p!=0:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.getLength() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = 0

    def append(self, item):
        q = Node(item)
        if self.head == 0:
            self.head = q
            self.tail = q
        else:
            p = self.tail
            p.next = q
            self.tail = q

    def getItem(self, index):
        if self.is_empty():
            print('linklist is empty.')
            return
        j = 0
        p = self.head
        while p.next != 0 and j<index:
            p = p.next
            j += 1

        if j==index:
            return p.data
        else:
            print('Target is not exist.')

    def insert(self, index, newData):

        if self.is_empty() or index < 0 or index > self.getLength():
            print('Linklist is empty.')
            return

        if index == 1:
            q = Node(newData, self.head)
            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            node = Node(newData, p)
            post.next = node



    def delete(self, index):
        if self.is_empty() or index < 0 or index > self.getLength():
            print('Linklist is empty.')
            return

        if index == 0:
            self.head = self.head.next

        p = self.head
        post = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            post.next = p.next

    def index(self, value):
        if self.is_empty():
            print('linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data == value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


l = LinkList()
l.initList([i for i in range(1,6)])
# print([i for i in range(1,6)])
print(l.getItem(4))
l.append(7)
print(l.getItem(5))

l.insert(4, 10)
print(l.getItem(3))
print(l.getItem(4))
print(l.getItem(5))
# print(l.getItem(6))

l.delete(5)
print(l.getItem(5))

l.index(5)



# Test a loop in linked list
class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    @classmethod  # the decorator use as a Factory
    def count(cls, a):
        return cls(a)

def isCycled(head):
    slowP = fastP = head
    n = 0
    while (slowP and fastP and fastP.next):
        slowP = slowP.next
        fastP = fastP.next.next
        n += 1
        if slowP == fastP:
            print("The loop is found! {} times search.\n".format(n))
            return True

    print('There is no loop in the linked list!\n')
    return False

def creatNode():
    listNodes = []
    for i in range(10):
        node = ListNode(i)
        listNodes.append(node)

    for i, node in enumerate(listNodes):
        node.next = listNodes[(i+1)%10]
    return listNodes

# Test Case
listNodes = creatNode()
isCycled(listNodes[0])


def rangeBitwiseAnd(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    r = m
    for j in range(m + 1, n + 1):
        r = r & j

    return r

