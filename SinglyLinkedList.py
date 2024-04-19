class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end = ", ")
            current = current.next
        print("None")

    def remove(self, position):
        if position == 0:
            if self.head:
                self.head = self.head.next
            else:
                print("List is empty")

        else:
            current = self.head
            prev = None
            count = 0
            while current and count < position:
                prev = current
                current = current.next
                count += 1
            if current:
                prev.next = current.next
            else:
                print("Position not found")

    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0 
            while current and count < position:
                prev = current
                current = current.next
                count += 1
            if current:
                prev.next = new_node
                new_node.next = current.next
            else:
                print("Position not found")
            
    def pop_back(self):
        if not self.head:
            print("List is empty")
        elif not self.head.next:
            self.head = None
        else:
            current = self.head
            prev = None
            while current.next:
                prev = current
                current = current.next
            prev.next = None

    def clear(self):
        self.head = None

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

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

def merge(ll1, ll2):
    merged = SinglyLinkedList()
    current_ll1 = ll1.head
    current_ll2 = ll2.head
    while current_ll1 and current_ll2:
        if current_ll1.data < current_ll2.data:
            merged.push_back(current_ll1.data)
            current_ll1 = current_ll1.next
            
        else:
            merged.push_back(current_ll2.data)
            current_ll2 = current_ll2.next

    while current_ll1:
        merged.push_back(current_ll1.data)
        current_ll1 = current_ll1.next

    while current_ll2:
        merged.push_back(current_ll2.data)
        current_ll2 = current_ll2.next

    return merged


# linked_list = SinglyLinkedList()
# linked_list.push_back(10)
# linked_list.push_back(20)
# linked_list.push_back(30)

# linked_list.traverse()  

# linked_list.reverse()
# linked_list.traverse()

# linked_list.remove(1)
# linked_list.traverse()

# linked_list.insert(1, 25)
# linked_list.traverse()  

# linked_list.pop_back()
# linked_list.traverse()  

# linked_list.clear()
# linked_list.traverse() 

# linked_list2 = SinglyLinkedList()
# linked_list2.push_back(5)
# linked_list2.push_back(15)
# linked_list2.push_back(25)

# linked_list2.traverse()

# merged_list = merge(linked_list, linked_list2)
# print("Merged list:")
# merged_list.traverse()


# linked_list3 = SinglyLinkedList()
# linked_list3.push_back(6)
# linked_list3.push_back(1)
# linked_list3.push_back(77)

# linked_list3.selection_sort()
# linked_list3.traverse()