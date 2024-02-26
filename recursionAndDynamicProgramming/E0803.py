from typing import List

class E0803:
    def findMagicIndex(self, nums: List[int]) -> int:
        return self.recursive(0, nums)
    
    def recursive(self, index: int, nums: List[int]) -> int:
        num = nums[index]
        if index == num:
            return index
        if num > index and num < len(nums):
            return self.recursive(num, nums)
        if index + 1 < len(nums):
             return self.recursive(index + 1, nums)
        
        return -1
        
a = E0803()
print(a.findMagicIndex([0, 2, 3, 4, 5]))
print(a.findMagicIndex([1, 1, 1]))
print(a.findMagicIndex([-96, -87, -76, -66, -64, -57, -8, 4, 8, 27, 39, 48, 52, 62, 63, 69, 84, 85, 85, 90]))