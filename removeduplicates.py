class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def print_linked_list(head):
    current = head
    while current:
        print(current.data, ed="->")   
        current = current.next
    print("None")


def remove_duplicate(head):
    if head is None:
        return

    unique_set = set()
    current = head
    prev = None

    while current:
        if current.data in unique_set:
            prev.next = current.next
        else:
            unique_set.add(current.data)
            prev = current
        current = current.next

# Sample input linked list creation
head = Node(2)
head.next = Node(5)
head.next.next = Node(12)
head.next.next.next = Node(2)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(1)
head.next.next.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next.next.next = Node(5)

print("Original Linked List:")
print_linked_list(head)

remove_duplicates(head)

print("\nLinked List after removing duplicates:")
print_linked_list(head)
# Output:







