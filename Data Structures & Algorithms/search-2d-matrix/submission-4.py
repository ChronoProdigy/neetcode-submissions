class Solution:
    def binary_search(self, numbers: List[int], target: int) -> bool:
        low = 0
        high = len(numbers) - 1

        while low <= high:
            mid = (low + high) // 2
            print(mid)
            mid_val = numbers[mid]

            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerLow = 0
        outerHigh = len(matrix) - 1

        if len(matrix) == 1:
            return self.binary_search(matrix[0], target)

        while outerLow <= outerHigh:
            outer_mid = (outerLow + outerHigh) // 2
            mid_val_start = matrix[outer_mid][0]
            mid_val_end = matrix[outer_mid][-1]

            if mid_val_start == target or mid_val_end == target:
                return True
            
            if mid_val_start < target < mid_val_end:
                #binary search this array for the target
                found = self.binary_search(matrix[outer_mid], target)
                if found:
                    return True
                else:
                    return False
            elif mid_val_end < target:
                outerLow = outer_mid + 1
            else:
                outerHigh = outer_mid - 1
        return False