class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] stores the number of ways to decode s[:i]
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            # Check if single digit decode is possible (1-9)
            if s[i-1] != '0':
                dp[i] += dp[i-1]
                
            # Check if two digit decode is possible (10-26)
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]