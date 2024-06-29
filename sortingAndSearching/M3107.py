from typing import List

class M3107:
    def minOperationsToMakeMedianKShort(self, nums: List[int], k: int) -> int:
        list_size = len(nums)
        nums.sort()
                # For i from 0 to medium index, the offset from the medium number should be non-positive,
                # For i from medium index to len(nums) -1, the offset from the medium number should be non-negative,
        return sum(max(nums[i] - k, 0) for i in range(list_size // 2 + 1)) + \
               sum(max(k - nums[i], 0) for i in range(list_size // 2, list_size))
    
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums = sorted(x - k for x in nums)
        list_size = len(nums)
        mid_index = list_size // 2 

        min_ops = 0
        for i in range(mid_index, list_size):
            if i == mid_index:
                min_ops += abs(nums[i])
                nums[i] = 0
            else: 
                neg_index = list_size - 1 -i if list_size % 2 == 1 else list_size -i
                if nums[i] < nums[i -1]:
                    min_ops += nums[i-1] - nums[i]
                    nums[i] = nums[i -1]
                elif nums[neg_index] > nums[neg_index + 1]:
                    min_ops += nums[neg_index] - nums[neg_index + 1]
                    nums[neg_index] = nums[neg_index + 1]
        
        if list_size % 2 == 0:
            if nums[0] > nums[1]:
                min_ops += nums[0] - nums[1]
                nums[0] = nums[1]

        return min_ops
    

# a = [3,2,1]
# a.sort()
# a = list(map(lambda x: x - 1, a))
# print(a)
a = M3107()
print(a.minOperationsToMakeMedianK([2,5,6,8,5], 4))
print(a.minOperationsToMakeMedianK([2,5,6,8,5], k = 7))
print(a.minOperationsToMakeMedianK([1,2,3,4,5,6], k = 4))
print(a.minOperationsToMakeMedianK([45,50,89,30,4,5,91,58], k = 31)) # 33