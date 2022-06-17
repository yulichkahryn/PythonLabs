class DoublyLinkedList:
    class Node:
        def __init__(self, content) -> None:
            self.content = content
            self.child = None
            self.parent = None

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push_back(self, content) -> None:
        if self.tail is None:
            self.tail = self.Node(content)
            self.head = self.tail
        else:
            self.tail.child = self.Node(content)
            self.tail.child.parent = self.tail
            self.tail = self.tail.child

    def sort_by_selection(self) -> None:
        tmp = self.head
        while tmp is not None:
            tmp1 = tmp.child
            while tmp1 is not None:
                if tmp1.content < tmp.content:
                    tmp1.content, tmp.content = tmp.content, tmp1.content
                tmp1 = tmp1.child
            tmp = tmp.child

    def print_list(self) -> None:
        node = self.head
        while node is not None:
            print(node.content)
            node = node.child

    def print_by_mark(self, mark: str) -> None:
        node = self.head
        while node is not None:
            if node.content.mark == mark:
                print(node.content)
            node = node.child

    def find_by_key(self, key) -> bool:
        node = self.head
        while node is not None:
            if node.content == key:
                return True
            node = node.child
        return False

    def pop_back(self) -> None:
        if self.tail is not None:
            self.tail = self.tail.parent
            self.tail.child = None
            if self.head.child is None:
                self.head = None

    def pop_front(self) -> None:
        if self.head is not None:
            self.head = self.head.child
            self.head.parent = None
            if self.tail.parent is None:
                self.tail = None

    def delete_by_key(self, key) -> None:
        if self.head is None:
            return
        if self.head.content == key:
            self.pop_front()
            return
        if self.tail.content == key:
            self.pop_back()
            return

        node = self.head
        while node.child is not None:
            if node.content == key:
                node.child.parent = node.parent
                node.parent.child = node.child
                return
            node = node.child

    def clear(self):
        while self.tail is not None:
            if self.tail.parent is None:
                self.tail, self.head = None, None
            else:
                tmp = self.tail.parent
                self.tail.parent = None
                self.tail = tmp
                self.tail.child = None

