class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # G[n] will store the number of unique BSTs for n nodes
        G = [0] * (n + 1)
        
        # Base cases
        G[0] = 1 # An empty tree is 1 way
        G[1] = 1 # A single node is 1 way
        
        # Calculate for each number of nodes from 2 up to n
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                # G(n) = sum_{i=1}^{n} G(i-1) * G(n-i)
                G[nodes] += G[root - 1] * G[nodes - root]
                
        return G[n]