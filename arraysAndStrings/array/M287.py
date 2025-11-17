from typing import List

class M287:
    def findDuplicateSort(self, nums: List[int]) -> int:
        nums.sort()
        prev_num = nums[0]
        for i in range(1, len(nums), 1):
            if nums[i] == prev_num:
                return prev_num
            else:
                prev_num = nums[i]
        return prev_num

    def findDuplicateBinarySearch(self, nums: List[int]) -> int:
        n = len(nums) - 1
        lo, hi = 1, n
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            num_sum = 0 
            for i in range(len(nums)):
                if nums[i] <= mid:
                    num_sum += 1
            
            if num_sum > mid:
                hi = mid
            else:
                lo = mid + 1
            
        return lo
    
    def findDuplicateFastSlow(self, nums: List[int]) -> int:
        slow = 0 
        fast = 0
        started = False
        while not started or fast != slow:
            if not started:
                started = True
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]

        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return fast
    
    def findDuplicateIndexSort(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                else:
                    tmp = nums[nums[i] -1]
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = tmp

    def findDuplicateMarkValues(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] = - nums[abs(nums[i]) - 1]

    def findDuplicateHashSet(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return num
            else:
                hash_set.add(num)

    def findDuplicateCounts(self, nums: List[int]) -> int:
        counts = [0 for _ in range(len(nums))]
        for num in nums:
            counts[num - 1] += 1
            if counts[num - 1] > 1:
                return num
    
    def findDuplicateBruteForce(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
                
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        digit = n
        bit_count = 0
        while digit > 0:
            digit = digit >> 1
            bit_count += 1
        
        ans = 0
        for b in range(bit_count):
            x, y = 0, 0
            for i in range(1, n + 1):
                i = i >> b
                y += i % 2

            for num in nums:
                num = num >> b
                x += num % 2
            
            if x > y:
                ans += (1 << b)
        return ans

    
a = M287()
print(a.findDuplicate([1,3,4,2,2])) # 2
print(a.findDuplicate([3,1,3,4,2])) # 3
print(a.findDuplicate([3,3,3,3,3])) # 3
print(a.findDuplicate([1,4,4,2,4])) # 4
print(a.findDuplicate([8,7,1,10,17,15,18,11,16,9,19,12,5,14,3,4,2,13,18,18])) # 18
