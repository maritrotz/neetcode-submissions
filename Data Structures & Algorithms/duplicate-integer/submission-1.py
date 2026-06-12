class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_vals = set()
        for n in nums:
            if n in seen_vals:
                return True
            seen_vals.add(n)
        return False
         