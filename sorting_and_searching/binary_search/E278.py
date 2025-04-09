def isBadVersion(version: int) -> bool:
    """The isBadVersion API is already defined for you."""
    return True if version >= 1 else False

class E278:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo if isBadVersion(lo) else lo - 1
    
a = E278()
print(a.firstBadVersion(5)) # 4
print(a.firstBadVersion(1)) # 1
