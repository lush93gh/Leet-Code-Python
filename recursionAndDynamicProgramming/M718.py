from typing import List


class M718:
    def rollingHash(self, nums: List[int], length: int) -> list[int]:
        P = 101
        MOD = pow(2, 64)
        hash_list = [0 for _ in range(len(nums) - length + 1)]
        if length == 0:
            return hash_list
        hash = 0
        power = 1
        for i in range(len(nums)):
            if i < length - 1:
                hash = (hash * P + nums[i]) % MOD
                power = (power * P) % MOD
            else:
                hash_list[i - (length - 1)] = (hash * P + (nums[i]) % MOD ) % MOD
                hash = (
                    hash_list[i - (length - 1)] - nums[i - (length - 1)] * power
                ) % MOD

        return hash_list

    def checkLength(self, nums1: List[int], nums2: List[int], length: int) -> bool:
        hash_starting_indexes = {}
        for idx, hash in enumerate(self.rollingHash(nums1, length)):
            indexes = hash_starting_indexes.get(hash, [])
            indexes.append(idx)
            hash_starting_indexes[hash] = indexes

        for idx2, hash in enumerate(self.rollingHash(nums2, length)):
            for idx1 in hash_starting_indexes.get(hash, []):
                retult = nums1[idx1 : idx1 + length] == nums2[idx2 : idx2 + length]
                if retult:
                    return True
        return False

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        lo, hi = 0, min(len(nums1), len(nums2)) + 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self.checkLength(nums1=nums1, nums2=nums2, length=mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1

    def findLengthLCS(self, nums1: List[int], nums2: List[int]) -> int:
        list_len_1 = len(nums1) + 1
        list_len_2 = len(nums2) + 1

        table = [[0 for _ in range(list_len_2)] for _ in range(list_len_1)]
        consecutive_table = [[0 for _ in range(list_len_2)] for _ in range(list_len_1)]

        for i in range(1, list_len_1):
            for j in range(1, list_len_2):
                if nums1[i - 1] == nums2[j - 1]:
                    consecutive_table[i][j] = consecutive_table[i - 1][j - 1] + 1
                    table[i][j] = max(
                        max(table[i - 1][j], table[i][j - 1]),
                        consecutive_table[i][j],
                    )
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])

        return table[list_len_1 - 1][list_len_2 - 1]

    def findLengthSimple(self, nums1: List[int], nums2: List[int]) -> int:
        list_len_1 = len(nums1) + 1
        list_len_2 = len(nums2) + 1

        table = [[0 for _ in range(list_len_2)] for _ in range(list_len_1)]

        for i in range(1, list_len_1):
            for j in range(1, list_len_2):
                if nums1[i - 1] == nums2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1

        return max(max(row) for row in table)


a = M718()
print(a.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7])) # 3
print(a.findLength(nums1=[0, 0, 0, 0, 0], nums2=[0, 0, 0, 0, 0])) # 5
print(a.findLength(nums1=[0, 1, 1, 1, 1], nums2=[1, 0, 1, 0, 1])) # 2
print(a.findLength(nums1=[1, 2, 3, 4, 5], nums2=[9, 8, 7, 6, 5])) # 1
print(a.findLength(nums1=[1, 0, 0, 0, 1], nums2=[1, 0, 0, 1, 1])) # 3
print(
    a.findLength(
        nums1=[0, 0, 0, 0, 0, 0, 1, 0, 0, 0], nums2=[0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    )
) # 9
print(
    a.findLength(
        nums1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], nums2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    )
) # 59

# print(a.checkLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7], length=3))
# print(a.checkLength(nums1=[0, 0, 0, 0, 0], nums2=[0, 0, 0, 0, 0], length=5))
# print(a.checkLength(nums1=[0, 1, 1, 1, 1], nums2=[1, 0, 1, 0, 1], length=2))
# print(a.checkLength(nums1=[1, 2, 3, 4, 5], nums2=[9, 8, 7, 6, 5], length=1))
# print(a.checkLength(nums1=[1, 0, 0, 0, 1], nums2=[1, 0, 0, 1, 1], length=1))
# print(
#     a.checkLength(
#         nums1=[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#         nums2=[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#         length=5,
#     )
# )
# print(
#     a.checkLength(
#         nums1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], nums2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
#         length=49,
#     )
# )

# print(
#     a.rollingHash(
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
#         49,
#     )
# )
