from typing import List
from collections import Counter

class M75:
    def sortColors(self, nums: List[int]) -> None:
        counts = Counter(nums)
        nums[:] = [color for color in [0, 1, 2] for _ in range(counts[color])]
    
    

a = M75()
a.sortColors(nums = [2,0,2,1,1,0])
a.sortColors(nums = [2,0,1])
