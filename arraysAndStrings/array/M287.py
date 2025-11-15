from typing import List

class M287:
    def findDuplicateSort(self, nums: List[int]) -> int:
        nums.sort()
        prev_num = nums[0]
        for i in range(1, len(nums), 1):
            if nums[i] == prev_num:
                return prev_num
            else:
                prev_num = nums[i]
        return prev_num

    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        lo, hi = 1, n
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            num_sum = 0 
            for i in range(len(nums)):
                if nums[i] <= mid:
                    num_sum += 1
            
            if num_sum > mid:
                hi = mid
            else:
                lo = mid + 1
            
        return lo
    
a = M287()
print(a.findDuplicate([1,3,4,2,2])) # 2
print(a.findDuplicate([3,1,3,4,2])) # 3
print(a.findDuplicate([3,3,3,3,3])) # 3
print(a.findDuplicate([1,4,4,2,4])) # 4
