class E69:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x + 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            square = mid * mid
            if square == x:
                return mid
            elif x > square:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
    
    def mySqrtLowerBound(self, x: int) -> int:
        lo, hi = 0, x + 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            square = mid * mid
            if x <= square:
                hi = mid
            else:
                lo = mid + 1
        return hi if hi * hi == x else hi - 1
    
a = E69()
print(a.mySqrt(0))
print(a.mySqrt(1))
print(a.mySqrt(4)) # 2
print(a.mySqrt(8)) # 2

