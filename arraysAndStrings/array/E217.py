class E217:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for num in nums:
            if num in set:
                return True
            else:
                set.add(num)
        return False