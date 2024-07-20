import random

class M382:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = self.head.val
        count = 0
        pointer = self.head
        while pointer is not None:
            count += 1
            dice = random.random()
            if dice <= 1 / count:
                result = pointer.val
            pointer = pointer.next
        return result