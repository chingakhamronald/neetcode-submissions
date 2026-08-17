class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      ROW, COL = len(matrix), len(matrix[0])
      l, r = 0, (ROW * COL) - 1

      while l <= r:
        mid = (l + r) // 2
        row, col = mid // COL, mid % COL

        if target < matrix[row][col]:
          r = mid - 1
        elif target > matrix[row][col]:
          l = mid + 1
        else:
          return True
      return False
        


        