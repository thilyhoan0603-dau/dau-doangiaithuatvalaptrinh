class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] # Stores indices
        max_area = 0
        # Add a zero at the end to flush the stack
        heights.append(0)
        
        for i in range(len(heights)):
            # While the current height is less than the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # width = current_index - index_of_previous_smaller - 1
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
                
            stack.append(i)
            
        # Optional: Restore heights if needed elsewhere
        heights.pop()
        return max_area
        