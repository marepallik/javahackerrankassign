class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def merge(list1, list2):
        merged_list = LinkedList()
        current1 = list1.head
        current2 = list2.head
        while current1 and current2:
            if current2.data < current2.data:
                merged_list.insert(current1.data)
                current1 = current1.next
            else:
                merged_list.insert(current1.data)
                current2 = current2.next
        while current1:
            merged_list.insert(current1.data)
            current1 = current1.next
        while current2:
            merged_list.insert(current2.data)
            current2 = current2.next
        return merged_list
    def sort(self):
        if not self.head or not self.head.next:
            return
        current = self.head
        while current:
            index =current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("null")


list1 = LinkedList()
list1.insert(25)
list1.insert(35)
list1.insert(12)
list1.insert(4)
list1.insert(36)
list1.insert(48)

list2 = LinkedList()
list2.insert(8)
list2.insert(32)
list2.insert(22)
list2.insert(45)
list2.insert(63)
list2.insert(49)

print("Linked-List-1:")
list1.display()
print("Linked-List-2:")
list2.display()

merged_list = LinkedList.merge(list1, list2)
merged_list.sort()

