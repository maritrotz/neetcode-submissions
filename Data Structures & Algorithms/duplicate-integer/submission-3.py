class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_vals = list()
        for n in nums:
            if n in seen_vals:
                return True
            seen_vals.append(n)
        return False
         