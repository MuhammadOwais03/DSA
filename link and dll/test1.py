from singleLinkedList import *

# Create a linked list
head = listNode(9)
head.append(8)
head.append(7)
head.append(6)
head.append(5)
head.append(4)
head.append(3)
head.append(2)
head.append(1)

print("Original: ", head)
sortSLL(head)

print("Sorted: ", head)

# head2 = listNode(1)
# head2.append(2)
# head2.append(2)
# head2.append(2)
# head2.append(2)
# # # Print the original linked list
# # print("Original linked list:")
# # head.traverse()

# # # Delete all instances of the value 6
# # head = deleteAllInstance(head, 6)

# # # Print the modified linked list
# # print("\nLinked list after deleting all instances of 6:")
# # if head is None:
# #     print("All Delete")
# # else:
# #     head.traverse()

# # count_ = count_x(head, 6)
# # print(count_)
# # head.traverse()
# # print()
# # del_tail(head)
# # head.traverse()


# # new = combine(head, head2)
# # new.traverse()

# # l1, l2 = splitList(head)
# # l1.traverse()
# # l2.traverse()

# circularLinkList(head)
# h = insClist(head, 11, 12)
# traverseCircular(h)
