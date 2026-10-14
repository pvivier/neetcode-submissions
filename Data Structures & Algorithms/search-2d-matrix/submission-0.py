class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        # find row

        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = (right + left) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
        if left > right:
            return False
        list_ = matrix[mid]

        left, right = 0, len(list_) - 1

        while left <= right:
            mid = (right + left) // 2

            if list_[mid] == target:
                return True
            elif list_[mid]> target:
                right = mid - 1
            elif list_[mid] < target:
                left = mid + 1
        return False

