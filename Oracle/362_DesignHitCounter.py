from collections import deque


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_hits = 0
        self.que = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.que or self.que[-1][0]!=timestamp:
            self.que.append([timestamp, 1])
        else:
            self.que[-1][1] += 1
        self.num_hits += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if len(self.que) == 0:
            self.num_hits = 0
        elif self.que[0][0] <= timestamp - 300:
            self.num_hits -= self.que[0][1]
            self.que.popleft()
            self.getHits(timestamp)
        return self.num_hits
        


# Your HitCounter object will be instantiated and called as such:
if __name__ == '__main__':

    obj = HitCounter()
    obj.hit(2)
    obj.hit(3)
    obj.hit(4)
    print(obj.getHits(300))
    print(obj.getHits(301))
    print(obj.getHits(302))
    print(obj.getHits(303))
    print(obj.getHits(304))
    obj.hit(501)
    print(obj.getHits(600))


"""
["HitCounter","hit",    "hit",  "hit",  "getHits"," getHits",   "getHits",  "getHits",  "getHits",  "hit",  "getHits"]
[[],            [2],    [3],    [4],    [300],      [301],          [302],  [303],      [304],      [501],  [600]]
"""