import math

class E0203:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
