from typing import List

class E283:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p, q = 0, 0
        while q < len(nums):
            if nums[q] != 0:
                tmp = nums[q]
                nums[q] = nums[p]
                nums[p] = tmp   
                p += 1
            q += 1
    
    def moveZeroesSubOptimal(self, nums: List[int]) -> None:
        p, q = 0, 0
        while q < len(nums):
            if nums[q] != 0:
                nums[p] = nums[q]
                p += 1
            q += 1
        while p < len(nums):
            nums[p] = 0
            p += 1


a=E283()
nums = [0, 1, 0, 3, 12]
a.moveZeroesSubOptimal(nums)
print(nums)
nums = [0]
a.moveZeroesSubOptimal(nums)
print(nums)
nums = [1]
a.moveZeroesSubOptimal(nums)
print(nums)
