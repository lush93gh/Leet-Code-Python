class E268:
    def missingNumber(self, nums) -> int:
        allSum = (len(nums) + 1) * len(nums) / 2
        return int(allSum - sum(nums))
    

a = E268()
print(a.missingNumber([3,0,1]))
