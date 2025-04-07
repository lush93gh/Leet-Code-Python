def guess(num: int) -> int:
    """
    @param num, your guess
    @return
    -1 if num is higher than the picked number
    1 if num is lower than the picked number
    otherwise return 0
    """
    pick = 1
    if num > pick:
        return -1
    elif num < pick: 
        return 1
    else:
        return 0

class E374:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            current_guess = guess(mid)
            if current_guess == 0:
                return mid
            elif current_guess == 1:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
    
    def guessNumberLowerBound(self, n):
        lo, hi = 1, n + 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            current_guess = guess(mid)
            if current_guess <= 0:
                hi = mid
            elif current_guess == 1:
                lo = mid + 1

        return hi if guess(hi) == 0 else hi - 1
    
a = E374()
print(a.guessNumber(10))
print(a.guessNumber(2))