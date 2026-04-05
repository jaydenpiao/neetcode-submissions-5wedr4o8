class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        given an arr of ints stones where stones[i] represents the weight of the ith stone

        want to run a simulation

        at each step we choose the two heaviest stones, weights x and y and smash them together

        if x == y, both stones are destroyed,

        if x < y the stone of weight x is destroyed and the stone of weight y has new weight y-x

        continue simulation until no more than one stone remaining

        return weight of last remaining stone or 0 if none remain

        so lets keep a max heap

        can iterate through each stone multiply by -1 so we get the max heap behavior

        make the heap

        then while there is >1 element in the heap
        pop two, do the comparison
        """

        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)

            if y != x:
                heapq.heappush(max_heap, y - x)

        return -max_heap[0] if max_heap else 0
