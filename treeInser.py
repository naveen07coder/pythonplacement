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
        if data > self.key:
            if self.key:
                self.rchild.search(data)
            else:
                print("Node not present in tree")


root = BST(2)
root.insert(10)
root.insert(20)
root.insert(30)
root.insert(5)
root.search(10)