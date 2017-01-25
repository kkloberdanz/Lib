class BST:
    def __init__(self):
        self.left  = None
        self.right = None
        self.data  = None

    def find(self, item):

        if self.data == None:
            return None
    
        if item == self.data:
            return self

        else:
            # Go left
            if item < self.data:
                if self.left == None:
                    return None
                else:
                    return self.left.find(item)

            # Go right
            else:
                if self.right == None:
                    return None
                else:
                    return self.right.find(item)
        

    def insert(self, item):

        if self.data == None:
            self.data = item

        if item < self.data:

            # end found, now insert
            if self.left == None:
                bst = BST()
                bst.data = item
                self.left = bst

            # recursive call, go left
            else:
                self.left.insert(item)

        elif item > self.data:

            # end found, now insert
            if self.right == None:
                bst = BST()
                bst.data = item
                self.right = bst

            # recursive call, go right
            else:
                self.right.insert(item)


    def items(self):
        s = []
        node = self
        while len(s) > 0 or node != None:
            if node != None:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                yield node
                node = node.right

    def __iter__(self):
        for item in self.items():
            yield item
        raise StopIteration
