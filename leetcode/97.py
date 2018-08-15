'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m=len(s1)
        n=len(s2)
        if m+n != len(s3):
            return False
        path = [[0]*(n+1)]*(m+1)
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0:
                    path[i][j]=1
                elif i==0:
                    path[i][j]=(s2[j-1] == s3[j-1]) and path[i][j-1]
                elif j==0:
                    path[i][j]=(s1[i-1] == s3[i-1]) and path[i-1][j]
                else:
                    path[i][j]=(path[i][j-1] and s2[j-1]==s3[i+j-1]) or \
                               (path[i-1][j] and s1[i-1]==s3[i+j-1])
        return path[m][n]==1


