from typing import List
import QuickSort
import HeapSort

class M912:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorter = QuickSort.QuickSort() if len(nums) < 10**4 else HeapSort.HeapSort()
        return sorter.sort(nums)
    
a = M912()
print(a.sortArray([5,2,3,1]))
print(a.sortArray([4,1,3,2,16,9,10,14,8,7]))
print(a.sortArray([5,1,1,2,0,0]))
print(a.sortArray([5,1,1,1,1,1,1,1,1,1]))

