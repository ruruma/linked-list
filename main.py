class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def in_the_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        return

    def print(self):
        if self.head is None:
            print("Linked List is empty")

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.in_the_end(1)
    ll.at_begining(5)
    ll.at_begining(90)
    ll.at_begining(110)
    ll.in_the_end(2)
    ll.print()