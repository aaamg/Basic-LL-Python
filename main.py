class Node(object):
  def __init__(self, data = None, next = None):
    self.next = next
    self.data = data 

class LinkedList(object):
  def __init__(self, head = None):
    self.head = head

  def append(self, data):
        new_node = Node(data)

        if self.head:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node
        else:
             self.head = new_node


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
print(node3.data)