from typing import List
from bisect import bisect_right
from bisect import bisect_left

class E704:
    def search(self, nums: List[int], target: int) -> int:
        # lo, hi = 0, len(nums) - 1
        # while lo <= hi:
        #     mid = lo + ((hi - lo) >> 1)
        #     candidate = nums[mid]
        #     if candidate == target:
        #         return mid
        #     elif target > candidate:
        #         lo = mid + 1
        #     else:
        #         hi = mid - 1
        # return -1
        return self.searchLowerBoundLibrary(nums, target)
    
    def searchUpperBound(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            candidate = nums[mid]
            if target >= candidate:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1 if lo > 0 and nums[lo - 1] == target else -1
    
    def searchUpperBoundLibrary(self, nums: List[int], target: int) -> int:
        lo = bisect_right(nums, target)
        return lo - 1 if lo > 0 and nums[lo - 1] == target else -1

    def searchLowerBound(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            candidate = nums[mid]
            if target <= candidate:
                hi = mid 
            else:
                lo = mid + 1
        return hi if hi < len(nums) and nums[hi] == target else -1
    
    def searchLowerBoundLibrary(self, nums: List[int], target: int) -> int:
        hi = bisect_left(nums, target)
        return hi if hi < len(nums) and nums[hi] == target else -1


a = E704()
print(a.search([-1, 0, 3, 5, 9, 12], 9)) # 4
print(a.search([-1, 0, 3, 5, 9, 12], 2)) # -1
