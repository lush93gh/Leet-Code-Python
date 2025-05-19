from typing import List

class E3024:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[2] + nums[0] <= nums[1]:
            return "none"
        elif nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
            return "isosceles"
        else:
            return "scalene"
        
a= E3024()
print(a.triangleType([3, 3, 3]))
print(a.triangleType([3, 4, 5]))
print(a.triangleType([8, 4, 2]))