class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        # pref[0] = 1, suff[3] = 1

        for i in range(1,n):
            pref[i] = nums[i - 1] * pref[i - 1]
            # pref[1] = nums[0](1) * pref[0](1). pref[1] = 1
            # pref[2] = nums[1](2) * pref[1](1). pref[2] = 2
            # pref[3] = nums[2](2) * pref[2](2). pref[3] = 4
        for i in range(n-2,-1,-1):
            suff[i] = nums[i + 1] * suff[i + 1]
            # suff[2] = nums[3](4) * suff[3](1). suff[2] = 4
            # suff[1] = nums[2](3) * suff[2](4). suff[1] = 12
            # suff[0] = nums[1](2) * suff[1](12). suff[3] = 24
        for i in range(n):
            res[i] = pref[i] * suff[i]
            # res[0] = pref[0](1) * suff[0](24) = 24
            # res[1] = pref[1](1) * suff[1](12) = 12
            # res[2] = pref[2](2) * suff[2](4) = 8
            # res[3] = pref[3](4) * suff[3](1) = 4
        
        return res

        
        