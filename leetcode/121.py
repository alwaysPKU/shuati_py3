class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0
        res=0
        for i,p in enumerate(prices):
            if i < len(prices)-1:
                if prices[i+1] <= prices[i]:
                    continue
                res = max(prices[i+1:])-p if max(prices[i+1:])-p>res else res
        return res