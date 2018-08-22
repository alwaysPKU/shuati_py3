class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle[-1]
        depth=len(triangle)
        for d in range(depth-2,-1,-1):
            for i in range(d+1):
                dp[i]=min(dp[i], dp[i+1]) + triangle[d][i]
        return dp[0]
