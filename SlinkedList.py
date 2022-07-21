class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def inserthead(self, newNode):
        temp = self.head
        self.head = newNode
        newNode.next = temp
        del temp

    def midinsert(self, newNode, pos):
        currentNode = self.head
        currentpos = 0
        while True:
            if currentpos ==pos:
                previousNode.next = newNode
                newNode.next = currentNode
                break

            previousNode = currentNode
            currentNode = currentNode.next
            currentpos=currentpos+1

    def middel(self, pos):
        currentNode = self.head
        currentpos = 0

        while True:
            if currentpos == pos:
                pass
                prevNode.next = currentNode.next
                currentNode.next = None
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentpos=currentpos+1





    def insertend(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            nextNode = self.head
            while True:
                if nextNode.next is None:
                    break
                nextNode = nextNode.next
            nextNode.next = newNode

    def delend(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

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
sl = SinglyLinkedList()
sl.insertend(fn)
sn = Node(20)
sl.insertend(sn)
tn = Node(30)
sl.insertend(tn)
ttn = Node(40)
sl.inserthead(ttn)
mid = Node(35)
sl.midinsert(mid, 3)
sl.middel( 3)
# sl.delend()
sl.prints()

