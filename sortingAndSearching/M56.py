from typing import List

class M56:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        results = []
        results.append(intervals[0])
        for i in range(1, len(intervals)):
            a, b = results[-1]
            c, d = intervals[i]
            
            if c > b:
                results.append(intervals[i])
            else:
                results[-1] = [a, max(b, d)]
        
        return results



a = M56()
print(a.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
print(a.merge(intervals = [[1,4],[4,5]]))