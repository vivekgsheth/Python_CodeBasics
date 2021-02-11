class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        print("LinkedList is empty")
        if self.head is None:
            return

        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        llstr = ''
        itr = self.get_last_node()
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print('LL in reverse: ', llstr)

    def get_last_node(self):
        if self.head is None:
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def insert_at_begining(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr =  self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
        
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if data_after == itr.data:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if data == itr.data:
                self.remove_at(count)
                break
            itr = itr.next
            count += 1

