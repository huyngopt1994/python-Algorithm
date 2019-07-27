from typing import List

hash_table = {}


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for j in range(1, rowIndex + 2):
            point = self.generate_per_point(rowIndex + 1, j)
            hash_table[(rowIndex + 1, j)] = point
            result.append(point)
        return result

    def generate_per_point(self, i, j):
        if (j == 1) or (i == j):
            return 1
        if hash_table.get((i, j)):
            return hash_table[(i, j)]
        return self.generate_per_point(i - 1, j - 1) + self.generate_per_point(i - 1, j)
