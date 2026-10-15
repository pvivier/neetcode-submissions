class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        lis = [matrix[i][0] for i in range(len(matrix))]

        left = 0
        right = len(lis) - 1

        while left < right:
            mid = (left + right) //2 +1
            if lis[mid] <= target:
                left = mid
            elif lis[mid]>target:
                right = mid-1
        print(matrix[left])
        
        lis = matrix[left]

        left = 0
        right = len(lis) - 1

        while left <= right:
            mid = (left + right) //2
            if lis[mid] < target:
                left = mid+1
            elif lis[mid]>target:
                right = mid-1
            elif lis[mid] == target:
                return True
        return False





        
        