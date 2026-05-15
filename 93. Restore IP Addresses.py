class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        def backtrack(start, path):
            # Goal: If we have 4 segments and reached the end of the string, it's valid
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # Choice: Try taking 1, 2, or 3 digits for the next segment
            for i in range(1, 4):
                if start + i > len(s):
                    break
                
                segment = s[start:start + i]
                
                # Check for validity:
                # 1. No leading zeros (unless the segment is "0")
                # 2. Number must be <= 255
                if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                
                path.append(segment)
                backtrack(start + i, path)
                path.pop() # Backtrack
                
        backtrack(0, [])
        return res