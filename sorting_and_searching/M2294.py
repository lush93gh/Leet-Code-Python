from typing import List

class M2294:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        nums.sort()
        min_size = 1
        current_min = nums[0]

        for num in nums:
            if num - current_min > k:
                current_min = num
                min_size += 1
        return min_size

a = M2294()
print(a.partitionArray([1, 4, 7, 3, 4], 2))
print(a.partitionArray([3,6,1,2,5], 2))
print(a.partitionArray([1,2,3], 1))
print(a.partitionArray([2,2,4,5], 0))