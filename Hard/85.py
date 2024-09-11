class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        matrix = [[int(col) for col in row] for row in matrix]

        def histogram_area(histogram):

            stack = []
            left = []
            right = []
            
            for i in range(len(histogram)):
                if(stack == []):
                    left.append(0)
                    stack.append(i)
                else:
                    while(stack != [] and histogram[i] <= histogram[stack[-1]]):
                        stack.pop()
                    if(stack == []):
                        left.append(0)
                    else:
                        left.append(stack[-1]+1)
                    stack.append(i)

            stack = []

            for i in range(len(histogram)-1,-1,-1):
                if(stack == []):
                    right.append(len(histogram)-1)
                    stack.append(i)
                else:
                    while(stack != [] and histogram[i] <= histogram[stack[-1]]):
                        stack.pop()
                    if(stack == []):
                        right.append(len(histogram)-1)
                    else:
                        right.append(stack[-1]-1)
                    stack.append(i)
            
            right.reverse()

            max_area = 0

            for i in range(len(histogram)):
                max_area = max(max_area,histogram[i]*(right[i] - left[i] + 1))

            return max_area

        def biggest_submatrix(matrix):
            
            area = 0
            histogram = [0 for i in range(len(matrix[0]))]

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if(matrix[i][j] == 0):
                        histogram[j] = 0
                    else:
                        histogram[j] += 1
                area = max(area, histogram_area(histogram))
                
            return area

        return biggest_submatrix(matrix)