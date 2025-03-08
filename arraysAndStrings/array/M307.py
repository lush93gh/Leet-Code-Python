from typing import List

class M307:

    def __init__(self, nums: List[int]):
        self.prefix_sum = nums
        self.diffs = {}
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i -1]

    def update(self, index: int, val: int) -> None:
        prev_prefix_sum = self.prefix_sum[index]
        current_prefix_sum = val if index == 0 else val + self.prefix_sum[index - 1]
        self.diffs[index] = self.diffs.get(index, 0) + current_prefix_sum - prev_prefix_sum

    def sumRange(self, left: int, right: int) -> int:
        diff_left = 0
        diff_right = 0
        for k in self.diffs.keys():
            print('k', k)
            if left - 1 >= k:
                diff_left += self.diffs[k]
            elif right >= k:
                diff_right += self.diffs[k]
        print('diff_left', diff_left)
        print('diff_right', diff_right)
        if left == 0:
            return self.prefix_sum[right] + diff_left + diff_right
        else:
            print(self.prefix_sum[right], self.prefix_sum[left - 1], diff_left, diff_right)
            return self.prefix_sum[right] - self.prefix_sum[left - 1] + diff_left + diff_right
        
a = M307([1, 3, 5])
print(a.prefix_sum)
print(a.sumRange(0, 2))
print(a.update(1, 2))
print(a.prefix_sum)
print(a.diffs)
print(a.sumRange(0, 2))
print('---')
a = M307([9,-8])
a.update(0, 3)
print(a.prefix_sum)
print(a.diffs)
print(a.sumRange(1,1))
