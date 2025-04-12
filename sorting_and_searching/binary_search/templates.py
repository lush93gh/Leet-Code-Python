class BinarySearch:
    def template_3(self, nums: list[int], target: int) -> int:
        """
        Finds the lower bound.
        """
        if len(nums) == 0:
            return -1
        
        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            mid = lo + ((hi - lo) >> 1)
            num = nums[mid]
            if target > num:
                lo = mid
            else:
                hi = mid
        print(lo, hi, nums[lo], nums[hi])
        if nums[hi] == target:
            return hi
        elif nums[lo] == target:
            return lo
        else:
            return -1
        
a = BinarySearch()
print(a.template_3([1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,5], 3))