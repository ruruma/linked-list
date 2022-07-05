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

    def print(self):
        if self.head is None:
            print("Linked List is empty")

        itr = self.head
        print(type(itr))
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.at_begining(5)
    ll.at_begining(90)
    ll.at_begining(110)
    ll.print()