class E69:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low <= high:
            mid = low + (high - low) / 2
            square = mid * mid
            if square < x:
                low = mid + 1
            elif square > x:
                high = mid - 1
            else:
                return mid
            
        return high

