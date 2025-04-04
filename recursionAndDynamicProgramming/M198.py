from typing import List

class M198:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(nums)):
            if i == 0:
                a = nums[0]
            elif i == 1:
                b = max(nums[i], a)
            else:
                c = max(a + nums[i], b) 
                a = b
                b = c
        return max(a, b)
    
a = M198()
print(a.rob([1, 2, 3, 1])) # 4
print(a.rob([2, 7, 9, 3, 1])) # 12
print(a.rob([2, 1, 1, 2])) # 4
