class Solution(object):
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Check memoization table
        state = (s1, s2)
        if state in self.memo:
            return self.memo[state]
        
        # Base Cases
        if s1 == s2:
            self.memo[state] = True
            return True
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.memo[state] = False
            return False
            
        n = len(s1)
        
        for i in range(1, n):
            # Case 1: No Swap
            # s1: [---left---][---right---]
            # s2: [---left---][---right---]
            if (self.isScramble(s1[:i], s2[:i]) and 
                self.isScramble(s1[i:], s2[i:])):
                self.memo[state] = True
                return True
                
            # Case 2: Swap occurred
            # s1: [---left---][---right---]
            # s2: [---right---][---left---]
            if (self.isScramble(s1[:i], s2[n-i:]) and 
                self.isScramble(s1[i:], s2[:n-i])):
                self.memo[state] = True
                return True
        
        self.memo[state] = False
        return False