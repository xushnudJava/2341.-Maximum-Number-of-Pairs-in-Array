class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = set(nums)
        c,k = 0,0
        nums = sorted(nums)
        for i in num:
            t1 = 0
            for j in nums:
                if i == j:
                    t1 += 1
                elif t1 > 0:
                    break
            c += t1 // 2
            k += t1 % 2
        return [c,k]