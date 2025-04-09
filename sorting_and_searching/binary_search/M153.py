from typing import List

class M153:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while nums[lo] > nums[hi]:
            mid = lo + ((hi - lo) >> 1)
            num = nums[mid]
            if num >= nums[lo]:
                lo = mid + 1
            elif num <= nums[hi]:
                hi = mid
        return nums[lo]
    
a = M153()
print(a.findMin([3, 4, 5, 1, 2])) # 1
print(a.findMin([4, 5, 6, 7, 0, 1, 2])) # 0
print(a.findMin([11, 13, 15, 17])) # 11
