import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
        def __init__(self, node_data):
            self.data = node_data
            self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next

        if node:
            fptr.write(sep)

def condense(head):
    linkL = []
    lnk1 = set(head)
    print(lnk1)


head_count = int(input().strip())
head = SinglyLinkedList()

for _ in range(head_count):
    head_item = int(input().strip())
    head.insert_node(head_item)

result = condense(head.head)

