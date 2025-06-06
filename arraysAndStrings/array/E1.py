from typing import List

class E1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            if target - num in table.keys():
                return [i, table[target - num]]
            table[num] = i

        return [0, 0]
    
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if target - num == nums[j]:
                    return [i, j]
        return []

    def twoSumSort(self, nums: List[int], target: int) -> List[int]:
        table = [(num, idx) for idx, num in enumerate(nums)]
        table = sorted(table)
        p, q = 0, len(nums) - 1

        while p < q:
            if table[p][0] + table[q][0] == target:
                return [table[p][1], table[q][1]]
            if table[p][0] < target - table[q][0]:
                p += 1
            if table[q][0] > target - table[p][0]:
                q -= 1

        return [table[p][1], table[q][1]]

a = E1()
print(a.twoSum(nums=[2, 7, 11, 15], target=9)) # [0, 1]
print(a.twoSum(nums=[3, 2, 4], target=6)) # [1, 2]
print(a.twoSum(nums=[3, 3], target=6)) # [0, 1]
print(a.twoSum(nums=[0, 4, 3, 0], target=0)) # [0, 3]

