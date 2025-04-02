from typing import List

class E485:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        global_max = 1 if nums[0] == 1 else 0
        local_max = 1 if nums[0] == 1 else 0
        for idx in range(1, len(nums)):
            num = nums[idx]
            if num == 1:
                local_max += 1
                global_max = max(global_max, local_max)
            else:
                local_max = 0
                    
        return global_max
    
a = E485()
print(a.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(a.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
