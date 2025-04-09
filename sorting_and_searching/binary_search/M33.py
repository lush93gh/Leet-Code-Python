from typing import List

class M33:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while nums[lo] > nums[hi]:
            mid = lo + ((hi - lo) >> 1)
            num = nums[mid]
            if num == target:
                return mid
            elif num > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        offset = lo
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            adjusted_mid = (mid + offset) % len(nums)
            num = nums[adjusted_mid]
            if target == num:
                return adjusted_mid
            elif target > num:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi if nums[hi] == target else -1

    
    def binarySearch(self, nums: List[int], target: int, lo: int, hi: int) -> int:
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            num = nums[mid]
            if num == target:
                return mid
            elif target > num:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi if nums[hi] == target else -1
    
    def searchByCase(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            if nums[lo] <= nums[hi]:
                return self.binarySearch(nums, target, lo, hi)
            else:
                mid = lo + ((hi - lo) >> 1) 
                num = nums[mid]
                if num == target:
                    return mid
                elif target > num:
                    if num >= nums[lo]:
                        lo = mid + 1
                    elif num <= nums[hi]:
                        search_left = self.binarySearch(nums, target, mid + 1, hi)
                        if search_left != -1:
                            return search_left
                        hi = mid - 1
                else: 
                    if num >= nums[lo]:
                        search_right = self.binarySearch(nums, target, lo, mid - 1)
                        if search_right != -1:
                            return search_right 
                        lo = mid + 1
                    elif num <= nums[hi]:
                        hi = mid - 1 
        return hi if nums[hi] == target else -1
    
a = M33()
print(a.search(nums=[3, 1], target=4)) # -1
print(a.search(nums=[3, 1], target=0)) # -1
print(a.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)) # 4
print(a.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)) # -1
print(a.search(nums=[1], target=0)) # -1
print(a.search(nums=[1, 3], target=0)) # -1
print(a.search(nums=[1, 3], target=2)) # -1
print(a.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=8)) # 4
print(a.search(nums=[57,58,59,62,63,66,68,72,73,74,75,76,77,78,80,81,86,95,96,97,98,100,101,102,103,110,119,120,121,123,125,126,127,132,136,144,145,148,149,151,152,160,161,163,166,168,169,170,173,174,175,178,182,188,189,192,193,196,198,199,200,201,202,212,218,219,220,224,225,229,231,232,234,237,238,242,248,249,250,252,253,254,255,257,260,266,268,270,273,276,280,281,283,288,290,291,292,294,295,298,299,4,10,13,15,16,17,18,20,22,25,26,27,30,31,34,38,39,40,47,53,54], target=30)) 
# # 113
