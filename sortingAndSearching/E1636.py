from typing import List
from collections import Counter

class E1636:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))


a = E1636()
print(a.frequencySort(nums = [1,1,2,2,2,3]))
print(a.frequencySort(nums = [2,3,1,3,2]))