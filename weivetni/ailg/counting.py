from typing import List

"""
Counting
Given a list of urls, print out the top 3 frequent filenames.
ex.
Given
urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]
The program should print out
a.txt 3
b.txt 2
c.jpg 2
"""
class Counting:
    def count(self, urls: List[str]):
        file_counter = {}
        for url in urls:
            file_name = url.split("/")[-1]
            file_count = file_counter.get(file_name, 0)
            file_counter[file_name] = file_count + 1
        
        file_counter_sorted = {k: v for k, v in sorted(file_counter.items(), key=lambda x: -x[1])}
        for idx, (k, v) in enumerate(file_counter_sorted.items()):
            if idx < 3:
                print(k, v)

a = Counting()
a.count(urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
])
