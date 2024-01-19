class E217(object):
    def containsDuplicate(self, nums):
        set1 = set()
        for num in nums:
            if num in set:
                return True
            else:
                set.add(num)
        return False