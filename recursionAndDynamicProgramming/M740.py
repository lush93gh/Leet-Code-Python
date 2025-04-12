from typing import List
import queue

class M740:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            count = num_counts.get(num, 0) + num
            num_counts[num] = count
        num_counts = dict(sorted(num_counts.items()))

        a, b = (0, 0), (0, 0) # (key, value) pair
        for idx, kv in enumerate(num_counts.items()):
            k, v = kv
            if idx == 0:
                a = (k, v)
            elif idx == 1:
                key = k
                value = max(v, a[1]) if k - a[0] == 1 else v + a[1]
                b = (key, value)
            else:
                value = max(v+ a[1], b[1]) if k - b[0] == 1 else v + b[1]
                a = b
                b = (k, value)
            # print(a, b) 
        return max(a[1], b[1])
    
    def recursive(self, idx: int, nums: List[int]) -> int:
        if len(nums) == 0 or idx >= len(nums):
            return 0

        removed = nums.copy()
        removed.remove(nums[idx])
        while nums[idx] - 1 in removed:
            removed.remove(nums[idx] - 1)
        while nums[idx] + 1 in removed:
            removed.remove(nums[idx] + 1) 

        new_idx = 0 if len(removed) < len(nums) else idx + 1

        return max(self.recursive(idx + 1, nums), nums[idx] + self.recursive(new_idx, removed))
    
    def deleteAndEarnRecursive(self, nums: List[int]) -> int: 
        return self.recursive(0, nums)

    def deleteAndEarnIterative(self, nums: List[int]) -> int:
        q = queue.Queue()
        nums.sort()
        for num in set(nums):
            removed = nums.copy()
            removed.remove(num)
            while num + 1 in removed:
                removed.remove(num + 1)
            while num - 1 in removed:
                removed.remove(num - 1)

            q.put((0, num, removed))
        global_max = 0
        mem = {}
        while not q.empty():
            for _ in range(q.qsize()):
                current_max, num, current_list = q.get()
                current_set = set(current_list)
                if len(current_set) <= 1:
                    global_max = max(global_max, current_max + num + sum(current_list))
                elif len(current_set) == 2:
                    key = tuple(current_set)
                    get_mem = mem.get(key, -1)
                    if get_mem != -1:
                        local_max = get_mem
                    else:
                        set_list = list(current_set) 
                        local_max = (
                            max(set_list[0], set_list[1])
                            if abs(set_list[0] - set_list[1]) == 1
                            else sum(current_list)
                        )
                        mem[key] = local_max
                    global_max = max(global_max, local_max)
                else:
                    for n in current_set:
                        removed = current_list.copy()
                        removed.remove(n)
                        while n + 1 in removed:
                            removed.remove(n + 1)
                        while n - 1 in removed:
                            removed.remove(n - 1)

                        q.put((current_max + num, n, removed)) 

        return global_max
    
a = M740()
print(a.deleteAndEarn([3, 4, 2])) # 6
print(a.deleteAndEarn([2, 2, 3, 3, 3, 4])) # 9
print(
    a.deleteAndEarn([8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1, 4])
) # 61
print(a.deleteAndEarn([1])) # 1
print(a.deleteAndEarn([1,8,5,9,6,9,4,1,7,3,3,6,3,3,8,2,6,3,2,2,1,2,9,8,7,1,1,10,6,7,3,9,6,10,5,4,10,1,6,7,4,7,4,1,9,5,1,5,7,5])) 
# 138

    
