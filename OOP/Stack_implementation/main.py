from stack import Stack
from Linked_list.node import Node
from Linked_list.linked_List import Linked_list

stack1 = Stack()

stack1.push("Hello")

stack1.push("Goodbye")

print(stack1.__str__())

print(stack1.peek())

stack1.pop()

print(stack1.__str__())

stack1.pop()

#stack1.pop()


Linked_list1 = Linked_list()

node1 = Node("Fred")
node2 = Node("Bob")
node3 = Node("Tom")
node4 = Node("Ebenezer")
node5 = Node("Beth")

Linked_list1.add_Node(node1)
Linked_list1.add_Node(node2)
Linked_list1.add_Node(node3)
Linked_list1.add_Node(node4)

for i in range(0,5):
    print(Linked_list1.get_Node_by_index(i))

Linked_list1.insert_Node_by_index(2,node5)

print("\n\n\n\n\n")

for i in range(0,6):
    print(Linked_list1.get_Node_by_index(i))

