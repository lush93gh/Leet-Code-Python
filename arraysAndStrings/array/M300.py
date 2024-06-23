from typing import List

class M300:
    def lengthOfLIS(self, nums: List[int]) -> int:
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
list = [0,1,0,3,2,3]
print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(a.lengthOfLIS([0,1,0,3,2,3]))
print(a.lengthOfLIS([7,7,7,7,7,7,7]))
