# class Node:
#     def __init__(self, data):
#         #Created Node
#         self.data = data
#         self.next = None
# class SingleLinkedList:
#
#     def __init__(self):
#         self.head  = None
#
#     def insert(self, newNode):
#
#         if self.head is None:
#             self.head = newNode
#
#         else:
#
#             lastNode = self.head
#
#             while True:
#                 if lastNode.next is None:
#                     break
#                 lastNode = lastNode.next
#             lastNode.next = newNode
#
#     def prints(self):
#         currnode = self.head
#         if currnode is None:
#             print("List is Empty")
#         else:
#             while True:
#                 if currnode is None:
#                     break
#                 print(currnode.data)
#                 currnode = currnode.next
#
#
#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):

        if self.head is None:
            self.head = newNode

        else:
#
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def prints(self):
        currNode = self.head
        if currNode is None:
            print("List is Empty")
        else:
            while True:
                if currNode is None:
                    break
                print(currNode.data)
                currNode = currNode.next

fn = Node("Naveen")
sl = SingleLinkedList()
sl.insert(fn)
sn = Node("Jagan")
sl.insert(sn)
tn = Node("Harsha")
sl.insert(tn)

sl.prints()
