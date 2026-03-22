class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListCreation:
    def linkedListCreation(self, head: ListNode) -> ListNode:
        fast = head
        current = head
        ans = head
        next_head = head

        while current != None:
            fast = fast.next.next if (fast and fast.next) else None
            if next_head == current:
                next_head = next_head.next
            if current.next:
                current.next.next = current.next.next.next if (current.next.next) else None
            if fast != None:
                current.next = fast
            else:
                current.next = next_head
                fast = next_head
            current = current.next
        return ans
    
a = LinkedListCreation()
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)
seven = ListNode(7)
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven

ans = a.linkedListCreation(one)

while ans != None:
    print(ans.val)
    ans = ans.next
