'''
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(res, s, [])
        return res

    def dfs(self, res, s, stringlist):
        if len(s) == 0: res.append(stringlist)
        for i in range(1, len(s)+1):
            if self.__boolean__(s[:i]):
                self.dfs(res, s[i:],stringlist+[s[:i]])

    def __boolean__(self,sub):
        l = len(sub)
        for i in range(l//2):
            if sub[i] != sub[l-1-i]:
                return False
        return True
