class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0
        res=0
        for i, p in enumerate(prices):
            if i<len(prices)-1:
                tmp=prices[i+1]-prices[i] if prices[i+1]-prices[i]>0 else 0
                res+=tmp
        return res