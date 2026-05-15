class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n, l = len(s1), len(s2), len(s3)
        
        # If lengths don't match, it's impossible
        if m + n != l:
            return False
        
        # dp[i][j] means s1[:i] and s2[:j] can form s3[:i+j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    # Only s2 can contribute to s3
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    # Only s1 can contribute to s3
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    # Can we get here by picking from s1 or picking from s2?
                    from_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                    from_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                    dp[i][j] = from_s1 or from_s2
                    
        return dp[m][n]