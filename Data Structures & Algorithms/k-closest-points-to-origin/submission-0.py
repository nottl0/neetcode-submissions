class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p1: List):
            d = pow((pow((p1[0]), 2) + pow((p1[1]), 2)), 0.5)
            return d
        minheap = []
        for point in points:
            minheap.append((distance(point), point))
        heapq.heapify(minheap)
        res = []
        while k > 0:
            _, point = heapq.heappop(minheap)
            res.append(point)
            k -= 1

        return res