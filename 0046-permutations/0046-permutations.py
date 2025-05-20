class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start=0):
            # If we've fixed all positions, add a copy of nums to result
            if start == len(nums):
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap current element with the start
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse for the next element
                backtrack(start + 1)
                # Backtrack (undo the swap)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack()
        return result
