# Stack object used for the LR(k) parser

class Node:
    def __init__(self, token):
        self.value = token
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ''
        while cur:
            out += str(cur.value.value) + '->'
            cur = cur.next
        return out[:-2]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value

    def push(self, token):
        node = Node(token)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            removed = self.head.next
            self.head.next = removed.next
            self.size -= 1
            return removed.value
        return None

    def append(self, tokens):
        for i in range(len(tokens)):
            token = tokens[i]
            self.push(token)
