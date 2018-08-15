class Solution:
    def permute(self, nums):
        """
        46. Permutations
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        self.br_permute(res, tmp, nums)
        return res

    def br_permute(self, res, tmp, nums):
        if len(tmp) == len(nums):
            res.append(tmp.copy())
        else:
            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                self.br_permute(res, tmp, nums)
                tmp.pop()

