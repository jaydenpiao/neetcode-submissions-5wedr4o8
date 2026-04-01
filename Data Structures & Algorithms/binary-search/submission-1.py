class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        given an array of distinct ints nums, sorted in ascending order, and int target

        search for target within nums
        if it exists, then return index, otherwise return 1

        brute force, for loop

        since we want log n time, should use binary search

        get length of nums, divide by 2 to get middle

        check if middle is target, if not then check if target is less or greater

        if less get middle of left side, if greater get middle of right side

        terminates when found, or when mid divided by 2 is 0 because we take floor

        actually lets use l and r pointers

        so we can always calculate mid easily

        so for 
        nums = [-1,0,2,4,6,8], target = 2
                l          r
                l      r
                   l   r
                   l r
        mid = 3 which is val 4
        since 2 less than we move r to mid

        calculate mid which is l + r // 2 = 0 + 3 // 2 = 1
        so mid = 1 which is 0
        its less so move l to mid

        mid is 1 + 3 = 4 // 2 = 2
        so this is correct

        imagine target is 1 so r would move to mid
        then mid = 1 + 2 // 2 = 1 which is 0
        so move l to mid which is 
        """

        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
            
        