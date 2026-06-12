class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_vals = {} # num value: index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in previous_vals:
                return [previous_vals[diff],i]
            previous_vals[n] = i
        