class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_back(self):
        if not self.head:
            return "List is empty"
        
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
    def push_front(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_front(self):
        if not self.head:
            return "List is empty"
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def print_head(self):
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end = ", ")
            current = current.next
        print("None")


    def print_tail(self):
        if not self.tail:
            print("List is empty")
            return

        current = self.tail
        while current:
            print(current.data, end = ", ")
            current = current.prev
        print("None")

    def clear(self):
        self.head = None
        self.tail = None

    def size(self):
        size = 0        
        current = self.head
        while current:
            size += 1
            current = current.next
        return size   

    def empty(self):
        return self.size() == 0


    def remove(self, position):
        if position == 0:
            self.pop_front()

        elif position == self.size() - 1:
            self.pop_back()
        
        else:
            count = 0
            current = self.head
            while current and count < position:
                current = current.next 
                count += 1

            if current:
                current.prev.next = current.next
                current.next.prev = current.prev

    def insert(self, position, data):
        new_node = Node(data)

        if position == 0:
            self.push_front(data)

        elif position == self.size() - 1:
            self.push_back(data)

        else:
            count = 0
            current = self.head
            while current and count < position:
                current = current.next 
                count += 1
            if current:
                current.prev.next = new_node
                new_node.prev = current.prev
                new_node.next = current
                current.prev = new_node


    def selection_sort(self):
        current = self.head

        while current:
            min_node = current
            temp = current.next

            while temp:
                if temp.data < min_node.data:
                    min_node = temp
                temp = temp.next

            if min_node != current:
                current.data, min_node.data = min_node.data, current.data
            
            current = current.next


def merge(dll1, dll2):
    if not dll1.head:
        return dll2
    elif not dll2.head:
        return dll1
    
    merged = DoublyLinkedList()
    current_dll1 = dll1.head
    current_dll2 = dll2.head

    while current_dll1 and current_dll2:
        if current_dll1.data < current_dll2.data:
            merged.push_back(current_dll1.data)
            current_dll1 = current_dll1.next
        else:
            merged.push_back(current_dll2.data)
            current_dll2 = current_dll2.next

    while current_dll1:
        merged.push_back(current_dll1.data)
        current_dll1 = current_dll1.next

    while current_dll2:
        merged.push_back(current_dll2.data)
        current_dll2 = current_dll2.next

    return merged




# def merge(doubly_ll_1, doubly_ll_2):
#     current_self = doubly_ll_1.head
#     current_other = doubly_ll_2.head

#     while current_self and current_other:
#         if current_self.data < current_other.data:
#             if current_self.next:
#                 current_self = current_self.next
#             else:
#                 current_self.next = current_other
#                 current_other.prev = current_self
#                 break
#         else:
#             if current_self.prev:
#                 current_self.prev.next = current_other
#                 current_other.prev = current_self.prev
#             else:
#                 doubly_ll_1.head = current_other
#                 current_other.prev = None
#             current_self.prev = current_other
#             temp = current_other.next
#             current_other.next = current_self
#             current_other = temp

def main():
    dll1 = DoublyLinkedList()

    dll1.push_back(3)
    dll1.push_back(9)
    dll1.push_back(12)

    print("Initial List:")
    dll1.print_head()

    dll1.push_front(1)
    dll1.push_back(15)

    print("After Adding Elements:")
    dll1.print_head()

    dll1.pop_front()
    dll1.pop_back()

    print("After Removing Elements:")
    dll1.print_head()

    dll1.insert(1, 6)

    print("After Insertion:")
    dll1.print_head()

    dll1.remove(2)

    print("After Removal:")
    dll1.print_head()

    dll1.selection_sort()

    print("Sorted List:")
    dll1.print_head()

    dll2 = DoublyLinkedList()
    dll2.push_back(2)
    dll2.push_back(8)
    dll2.push_back(11)

    merged_list = merge(dll1, dll2)

    print("Merged List:")
    merged_list.print_head()

    dll1.clear()

    print("Cleared List:")
    dll1.print_head()

if __name__ == "__main__":
    main()






