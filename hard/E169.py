from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = nums[0]
        max = -float('inf')
        grouped =  list(zip(Counter(nums).keys(), Counter(nums).values()))
        for num, count in grouped:
            if count > max:
                max = count
                result = num
        return result