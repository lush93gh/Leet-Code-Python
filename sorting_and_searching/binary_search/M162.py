from typing import List

class M162:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            num = nums[mid]
            left = nums[mid - 1] if mid > 0 else float('-inf')
            right = nums[mid + 1] if mid < len(nums) - 1 else float('inf')
            if num > left and num > right:
                return mid
            elif num > left and num < right:
                lo = mid + 1
            else: 
                hi = mid - 1

        return hi








a = M162()
print(a.findPeakElement([1, 2, 3, 1])) # 2
print(a.findPeakElement([1, 2, 1, 3, 5, 6, 4])) # 5
print(a.findPeakElement([3, 1, 2])) # 0