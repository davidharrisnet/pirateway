
class LinkedList:

    def __init__(self):
        self.head_node = None

    def __repr__(self):
        node = self.head_node
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self,node):
        self.head_node = node

    def add_end(self, new_node):
        end_node = self.head_node
        while True:
            if end_node.next == None:
                end_node.next = new_node
                break
            else:
                end_node = end_node.next

    def remove(self, data):
        if self.head_node.data == data:
            self.head_node = None
        else:
            prev_node = self.head_node
            curr_node = self.head_node.next
            while True:
                if curr_node.data == data:
                    prev_node.next = curr_node.next
                    break;
                else:
                    prev_node = curr_node
                    curr_node = curr_node.next

    def insert(self,node, new_node):
        if self.head_node.data == new_node.data:
            temp_node = self.head_node.next
            self.head_node.next = new_node
            new_node.next = temp_node
            return
        else:
            curr_node = self.head_node.next

            while True:
                if curr_node.data == node:
                    temp_node = curr_node.next
                    curr_node.next = new_node
                    new_node.next = temp_node
                    break
                else:
                    curr_node = curr_node.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

linked_list = LinkedList()

node = Node('1')
linked_list.add_first(node)

node = Node('2')
linked_list.add_end(node)

node = Node('3')
linked_list.add_end(node)

node = Node('4')
linked_list.add_end(node)
print(linked_list)

linked_list.remove('2')

linked_list.insert('3',Node('8'))
print(linked_list)
