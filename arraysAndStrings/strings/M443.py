from typing import List

class M443:
    def compress(self, chars: List[str]) -> int:
        slow = 0
        last_cahr = 'start'
        counter = 0

        for i in range(len(chars)):
            if last_cahr != chars[i] and counter > 0:
                chars[slow] = last_cahr
                slow += 1
                if counter > 1:
                    counts = str(counter)
                    for j in range(len(counts)):
                        chars[slow] = counts[j]
                        slow += 1
                counter = 0
            last_cahr = chars[i]
            counter += 1

        if counter > 0:
            chars[slow] = last_cahr
            slow += 1
            if counter > 1:
                counts = str(counter)
                for j in range(len(counts)):
                    chars[slow] = counts[j]
                    slow += 1

        return slow
    
a = M443()
print(a.compress(["a","a","b","b","c","c","c"]))
print(a.compress(["a"]))
print(a.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))