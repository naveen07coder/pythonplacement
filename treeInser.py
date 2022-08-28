class BST:
    def __init__(self, data):
        self.lchild = None
        self.key = data
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.data = data
            return

        if self.key == data:
            return

        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        elif data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)


    def search(self, data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.key:
                self.lchild.search(data)
            else:
                print("Node not present in tree")
        else:
            if data > self.key:
                if self.key:
                    self.rchild.search(data)
                else:
                    print("Node not present in tree")

    def preorder(self) :
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self) :
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self) :
        if self.lchild:
            self.lchild.inorder()
        if self.rchild:
            self.rchild.inorder()
        print(self.key, end=" ")


    def delete(self):


root= BST(10)
list = [6,3,1,6,98,3,7 ]
for i in range(len(list)):
    root.insert(list[i])

# # root.search(10)
root.preorder()
print("preorder")
root.inorder()
print("inorder")
root.postorder()
print("postorder")

