from typing import List

class M34:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            num = nums[mid]
            if target > num:
                lo = mid + 1
            else:
                hi = mid
        lower = hi if nums[hi] == target else -1

        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            num = nums[mid]
            if target >= num:
                lo = mid + 1
            else:
                hi = mid

        upper = hi - 1 if nums[hi - 1] == target else -1 

        return [lower, upper]
    
a = M34()
print(a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)) # 3, 4
print(a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)) # -1, -1
print(a.searchRange(nums=[], target=0)) # -1, -1
print(a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=5)) # 0, 0
            