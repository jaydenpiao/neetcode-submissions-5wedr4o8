class KthLargest:
    """
    find kth largest int in a stream of values, including duplicates
    [1,2,3,3]
    the 2nd largest is 3


    """

    def __init__(self, k: int, nums: List[int]):
        """
        inits the object given an integer k and stream of ints nums
        """
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self.k = k

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        """
        adds integer val to the stream and returns kth largest int in the stream

        could sort an array everytime but time complexity is tough

        could do a max heap
        """
        heapq.heappush(self.min_heap, val)
        
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
        
