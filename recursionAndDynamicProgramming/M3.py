import queue

class M3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        array = [float("-inf") for i in range(128)]
        left = 0
        max_length: int = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord("a")
            if array[index] >= left:
                left = array[index] + 1

            array[index] = right
            max_length = int(max(max_length, right - left + 1))

        return max_length


    def lengthOfLongestSubstringMap(self, s: str) -> int:
        map = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            if map.get(s[right], float('-inf')) < left:
                map[s[right]] = right
                max_length = max(max_length, right - left + 1)
            else:
                left = map[s[right]] + 1
                map[s[right]] = right
        
        return max_length


    def lengthOfLongestSubstringSet(self, s: str) -> int:
        character_set = set()
        left, right = 0, 0
        max_length = 0
        while right < len(s):
            if s[right] not in character_set:
                character_set.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[right] in character_set:
                    character_set.remove(s[left])
                    left += 1
                character_set.add(s[right])
            right += 1
        return max_length
            


    def lengthOfLongestSubstringQueue(self, s: str) -> int:
        q = queue.Queue()
        max_length = 0
        for c in s:
            if c not in q.queue:
                q.put(c)
            else:
                while not q.empty():
                    dropped_character = q.get()
                    if dropped_character == c:
                        q.put(c)
                        break
            max_length = max(max_length, q.qsize())
        return max_length
a = M3()
print(a.lengthOfLongestSubstring("abcabcbb")) # 3
print(a.lengthOfLongestSubstring("bbbbb")) # 1
print(a.lengthOfLongestSubstring("pwwkew")) # 3
print(a.lengthOfLongestSubstring(" ")) # 0


