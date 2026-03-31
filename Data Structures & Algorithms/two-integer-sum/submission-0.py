class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for i, num in enumerate(nums):
            subtractor = target - num
            if subtractor in idxs:
                return[idxs[subtractor], i]

            idxs[num] = i
            
        return []

