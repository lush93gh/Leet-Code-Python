from typing import List

class H4:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        isOdd = (len(nums1) + len(nums2)) % 2 == 1
        if len(nums1) == 0:
            return self.medium(nums2)
        if len(nums2) == 0:
            return self.medium(nums1)

        low1, high1 = 0, len(nums1) - 1
        low2, high2 = 0, len(nums2) - 1
        low, high = 0, len(nums1) + len(nums2) - 1
        lowVal, highVal = float('inf'), float('inf')
        while low < high:
            mid1 = low1 + ((high1 - low1) >> 1) 
            mid1 = min(len(nums1) - 1, max(0, mid1))
            mid_val_1 = nums1[mid1]
            mid2 = low2 + ((high2 - low2) >> 1) 
            mid2 = min(len(nums2) - 1, max(0, mid2))
            mid_val_2 = nums2[mid2]
            if mid_val_1 == mid_val_2:
                return mid_val_1
            elif mid_val_1 > mid_val_2:
                high -= high1 - (mid1 - 1)
                high1 = max(0, mid1 - 1)
                highVal = nums1[high1]
                low += mid2 + 1 - low2
                low2 = min(len(nums2) -1, mid2 + 1)
                lowVal = nums2[low2]
            else:
                low += mid1 + 1 - low1
                low1 = min(len(nums1) - 1, mid1 + 1)
                lowVal = nums1[low1]
                high -= high2 - (mid2 - 1)
                high2 = max(0, mid2 - 1)
                highVal = nums2[high2]

        if isOdd:
            return lowVal if lowVal < highVal else highVal
        else:
            return (lowVal + highVal) / 2
        
    def medium(self, nums: List[int]):
        midIndex = len(nums) // 2
        return nums[midIndex] if len(nums) % 2 == 1 else (nums[midIndex] + nums[midIndex-1]) / 2



    
a =H4()
print(a.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(a.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
print(a.findMedianSortedArrays(nums1 = [], nums2 = [1]))
print(a.findMedianSortedArrays(nums1 = [1,3], nums2 = [2,7]))
print(a.findMedianSortedArrays([1,3,6], [2,5]))
print(a.findMedianSortedArrays([], [2,3]))
        
        
