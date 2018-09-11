class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        leth=len(nums)
        if leth == 1:
            return nums[0]
        elif leth ==2:
            return max(nums)
        else:
            m2=nums[0]
            m1=max(nums[:2])
            res=0
            for i in range(2,leth):
                res=max(m2+nums[i], m1)
                m2=m1
                m1=res
            return res
