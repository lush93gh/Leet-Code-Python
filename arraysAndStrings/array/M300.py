from typing import List
from bisect import bisect_left


class M300:
    def lengthOfLIS(self, nums: List[int]) -> int:
        list = []

        for num in nums:
            index = self.binarySearch(list, num)
            if index == len(list):
                list.append(num)
            else:
                list[index] = num

        return len(list)
    
    def binarySearch(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            num = nums[mid]

            if num == target:
                return mid
            elif target < num:
                hi = mid -1
            else:
                lo = mid + 1
        
        return lo 

    def LCS(self, nums: List[int]) -> int:
        sorted_set = sorted(set(nums))
        list_size = len(nums)
        set_size = len(sorted_set)
        table = [[0 for i in range(list_size + 1)] for j in range(set_size + 1)]

        for i in range(1, set_size + 1):
            for j in range(1, list_size + 1): 
                if sorted_set[i -1] == nums[j -1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        
        return table[set_size][list_size]
     
a = M300()
# print(a.binarySearch([2], 5))
# print(a.binarySearchReversed([], 12))
print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(a.lengthOfLIS([0,1,0,3,2,3]))
print(a.lengthOfLIS([7,7,7,7,7,7,7]))
print(a.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

