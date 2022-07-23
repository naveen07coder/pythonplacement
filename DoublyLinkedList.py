class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delmid(self, pos):
        currentNode = self.head
        currentpos = 0

        while True:
            if currentpos == pos:
                prevNode.next = currentNode.next
                currentNode.prev = prevNode
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentpos = currentpos + 1


    def inHead(self, newNode):
        temp = self.head
        self.head = newNode
        newNode.next = temp
        temp.prev = newNode

    def Insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    lastNode.next = newNode
                    newNode.prev = lastNode
                    newNode.next = None
                    break
                lastNode = lastNode.next

    def insertMid(self, newNode, pos):
        currentNode = self.head
        currentpos = 0

        while True:
            if currentpos == pos:
                prevNode.next = newNode
                newNode.prev = prevNode

                newNode.next = currentNode
                currentNode.prev = newNode
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentpos = currentpos+1



    def insertend(self, newNode):
        lastnode = self.head
        while True:
            if lastnode.next is None:
                lastnode.next = newNode
                newNode.prev = lastnode.next
                newNode.next = None
                break
            lastnode = lastnode.next



    def prints(self):
        currentNode = self.head
        if currentNode is None:
            print("List is empty")
        else:
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next

fn = Node(10)
sl = DoublyLinkedList()
sl.Insert(fn)
sn = Node(20)
sl.Insert(sn)
tn = Node(30)
sl.Insert(tn)
lanode = Node(40)
sl.insertend(lanode)
midNode = Node(35)
sl.insertMid(midNode, 3)
top = Node(5)
sl.inHead(top)
sl.delmid(4)
sl.prints()