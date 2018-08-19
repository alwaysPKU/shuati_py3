'''
646. Maximum Length of Pair Chain
646. 最长数对链
'''
class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        res=0
        if not pairs:
            return 0
        pairs.sort(key=lambda x:x[0])
        small=pairs[0][0]-1
        big=pairs[0][0]-1
        for pair in pairs:
            if pair[0]>big:
                res+=1
                small=pair[0]
                big=pair[1]
            elif pair[1]<=big:
                small=pair[0]
                big=pair[1]
            else:
                continue
        return res

s=[[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
t=Solution()
res=t.findLongestChain(s)
print(res)
