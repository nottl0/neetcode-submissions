class MedianFinder:

    def __init__(self):
        self.heap = []
        self.outside = []
        heapq.heapify(self.heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        total_len = len(self.heap)
        k = total_len
        while k > total_len // 2:
            el = heapq.heappop(self.heap)
            self.outside.append(el)
            k -= 1
        if total_len % 2 == 0:
            new_el = heapq.heappop(self.heap)
            med = (el + new_el)/2
            self.outside.append(new_el)
        else:
            med = float(el)
    
        while len(self.outside) > 0:
            heapq.heappush(self.heap, self.outside[-1])
            del self.outside[-1]
        return med
        