from typing import List
import random

class M3107:
    def exchange(self, A: List, i: int, j: int):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    def partition(self, A: List, p: int, r: int) -> tuple[int, int]:
        pivot = A[r]
        i = p -1
        q1 = r
        for j in range(p, r):
            if A[j] == pivot:
                while q1 > j and A[q1] == pivot:
                    q1 -= 1
                self.exchange(A, j, q1)
            if A[j] < pivot:
                i += 1
                self.exchange(A, i, j)
        num_pivot = r - q1 + 1
        for index in range(i + 1, i + 1 + num_pivot):
            offset = index - (i + 1)
            self.exchange(A, index, q1 + offset)
        return i + 1, (i + 1 + num_pivot - 1)
    
    def randomizedPartition(self, A: List, p: int, r: int) -> tuple[int, int]:
        i = random.randint(p, r)
        self.exchange(A, i, r)
        return self.partition(A, p, r)
    
    def randomizedQuickMakeMedian(self, A: List, p: int, r: int)-> int:
        if p < r:
            mdeium_index = len(A) // 2
            q1, q2 = self.randomizedPartition(A, p, r)
            if q1 <= mdeium_index and mdeium_index <= q2:
                return mdeium_index
            elif q1 > mdeium_index:
                return self.randomizedQuickMakeMedian(A, p, q1 - 1)
            else:
                return self.randomizedQuickMakeMedian(A, q2 + 1, r)
        else:
            return r
        
    def randomizedQuickMakeMedianIterative(self, A: List)-> int:
        p = 0
        r = len(A) - 1
        mdeium_index = len(A) // 2
        q1 = q2 = r + 1
        while mdeium_index not in range(q1, q2 + 1):
            q1, q2 = self.randomizedPartition(A, p, r)
            if q1 > mdeium_index:
                r = q1 - 1
            else:
                p = q2 + 1

        return mdeium_index
        
    def minOperationsToMakeMedianKQuick(self, nums: List, k: int) -> int:
        q = self.randomizedQuickMakeMedianIterative(nums)
        num_ops = 0
        for i in range(q + 1):
            num_ops += max(nums[i] - k, 0)
        for i in range(q, len(nums)):
            num_ops += max(k - nums[i], 0)
        return num_ops
    
    def minOperationsToMakeMedianKShort(self, nums: List[int], k: int) -> int:
        list_size = len(nums)
        nums.sort()
                # For i from 0 to medium index, the offset from the medium number should be non-positive,
                # For i from medium index to len(nums) -1, the offset from the medium number should be non-negative,
        return sum(max(nums[i] - k, 0) for i in range(list_size // 2 + 1)) + \
               sum(max(k - nums[i], 0) for i in range(list_size // 2, list_size))
    
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums = sorted(x - k for x in nums)
        list_size = len(nums)
        mid_index = list_size // 2 

        min_ops = 0
        for i in range(mid_index, list_size):
            if i == mid_index:
                min_ops += abs(nums[i])
                nums[i] = 0
            else: 
                neg_index = list_size - 1 -i if list_size % 2 == 1 else list_size -i
                if nums[i] < nums[i -1]:
                    min_ops += nums[i-1] - nums[i]
                    nums[i] = nums[i -1]
                elif nums[neg_index] > nums[neg_index + 1]:
                    min_ops += nums[neg_index] - nums[neg_index + 1]
                    nums[neg_index] = nums[neg_index + 1]
        
        if list_size % 2 == 0:
            if nums[0] > nums[1]:
                min_ops += nums[0] - nums[1]
                nums[0] = nums[1]

        return min_ops
    

# a = [3,2,1]
# a.sort()
# a = list(map(lambda x: x - 1, a))
# print(a)
a = M3107()
print(a.minOperationsToMakeMedianKQuick([2,5,6,8,5], 4))
print(a.minOperationsToMakeMedianKQuick([2,5,6,8,5], k = 7))
print(a.minOperationsToMakeMedianKQuick([1,2,3,4,5,6], k = 4))
print(a.minOperationsToMakeMedianKQuick([45,50,89,30,4,5,91,58], k = 31)) # 33
print(a.minOperationsToMakeMedianKQuick([1,1,1,1,1,1,1,1,1,1,1,1,1,1], k = 2)) 