from typing import List

class M658:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if mid + k < len(arr) and x - arr[mid] > arr[mid + k] - x:
                print(mid, arr[mid], arr[mid + k - 1])
                lo = mid + 1
            else:
                hi = mid
                print(mid, arr[mid])

        return arr[hi: hi +k]

    def findClosestElementsUpperAndLowerBound(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            num = arr[mid]
            if x <= num:
                hi = mid
            else:
                lo = mid + 1

        lower = hi 
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            num = arr[mid]
            if x >= num:
                lo = mid + 1
            else:
                hi = mid

        upper = hi

        if lower == 0 and upper == 0:
            lower = 0
            upper = k 
        elif arr[lower] != x and lower + 1 == upper:
            upper = len(arr) 
            lower = len(arr) - k
        else:
            k -= upper - lower

            while k > 0:
                lower_candidate = arr[lower - 1] if lower - 1 >= 0 else float('inf')
                self_candidate = arr[lower] if lower == upper else float("inf") 
                upper_candidate = arr[upper] if upper < len(arr) else float('inf')

                lower_distance = abs(x - lower_candidate)
                self_distance = abs(x - self_candidate)
                upper_distance = abs(upper_candidate - x)

                min_distance = min(self_distance, lower_distance, upper_distance)
                if lower_distance == min_distance:
                    lower -= 1
                elif self_distance == min_distance:
                    upper += 1
                else:
                    upper += 1
                k -= 1

            while k < 0:
                upper -= 1
                k += 1

        return arr[lower:upper]

a = M658()
print(a.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))  # [1,2,3,4]
print(a.findClosestElements(arr=[1, 1, 2, 3, 4, 5], k=4, x=-1))  # [1,1,2,3]
print(a.findClosestElements(arr=[1, 1, 1, 10, 10, 10], k=1, x=9))  # [10]
print(a.findClosestElements(arr=[0, 0, 1, 2, 3, 3, 4, 7, 7, 8], k=3, x=5))  # [3,3,4]
print(a.findClosestElements(arr=[1, 1, 2, 3, 3, 3, 4, 6, 8, 8], k=6, x=1))  # [1,1,2,3,3,3]
print(a.findClosestElements(arr=[3, 5, 8, 10], k=2, x=15))  # [8,10]
print(a.findClosestElements(arr=[1, 3], k=1, x=2))  # [1]
print(a.findClosestElements(arr=[0, 0, 0, 1, 3, 5, 6, 7, 8, 8], k=2, x=2))  # [1,3]
print(a.findClosestElements(arr=[3, 3, 3, 3, 3, 3, 3, 3, 3], k=2, x=3))  # [3,3]
print(a.findClosestElements(arr=[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4], k=4, x=3))  # [2,2,3,3]