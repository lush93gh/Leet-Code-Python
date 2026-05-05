class Task3:
    def solution(self, A, L, R):
        l_indexs = []
        r_indexs = []
        for i in range(len(A)):
            num = A[i]
            if num == R:
                r_indexs.append(i)
            if num == L:
                l_indexs.append(i)
        
        min = float('inf')
        for ri in r_indexs:
            for li in l_indexs:
                candidate = li - ri 
                if candidate >= 0 and candidate < min:
                    min = candidate

        return -1 if min == float('inf') else min + 1 


a = Task3()
print(a.solution([3,2,4],4,3))
print(a.solution([2, 1, 4, 3, 2, 1, 1, 4],2,4))
print(a.solution([10**9, 1, 1, 1, 1, 1, 10**9- 1],10**9-1, 10**9))
print(a.solution([1, 3, 5, 7], 3, 5))