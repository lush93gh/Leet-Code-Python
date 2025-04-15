from typing import List

class M39:    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        aggerate_list = []
        for candidate in candidates:
            if target == candidate:
                aggerate_list.append([candidate])
            elif candidate < target:
                list_of_lists = self.combinationSum(candidates, target - candidate)
                for sub_list in list_of_lists:
                    sub_list.append(candidate)
                    sub_list.sort()
                    if sub_list not in aggerate_list:
                        aggerate_list.append(sub_list)

        return aggerate_list
    
a= M39()
print(a.combinationSum(candidates=[2, 3, 6, 7], target=7))  # [[2,2,3],[7]]
print(a.combinationSum(candidates=[2, 3, 5], target=8))  # [[2,2,2,2],[2,3,3],[3,5]]
print(a.combinationSum(candidates=[2], target=1))  # []
