from typing import List

class M213:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
             return nums[0]
        
        a, b, = 0, 0
        for i in range(len(nums) - 1):
            if i == 0:
                a = nums[i]
            elif i == 1:
                b = max(a, nums[i])
            else:
                c = max(nums[i] + a, b) 
                a = b
                b = c
        x = max(a, b)

        a, b = 0, 0
        for i in range(1, len(nums)):
            if i == 1:
                a = nums[i]
            elif i == 2:
                b = max(a, nums[i])
            else:
                c = max(nums[i] + a, b)
                a = b
                b = c
        y = max(a, b) 

        return max(x, y)
    

a = M213()
print(a.rob([2, 3, 2])) # 3
print(a.rob([1, 2, 3])) # 3
print(a.rob([1, 2, 3, 1])) # 4
print(a.rob([1,1])) # 1
print(a.rob([200, 3, 140, 20, 10])) # 340
print(a.rob([2, 7, 9, 3, 1])) # 11
print(a.rob([1, 2, 1, 1])) # 3
print(a.rob([2, 1, 1, 2])) # 3
print(a.rob([1, 1, 1, 2])) # 3
print(a.rob([2, 2, 4, 3, 2, 5])) # 10
print(a.rob([1])) # 1
        