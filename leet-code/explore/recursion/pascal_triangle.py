from typing import List

hash_table = {}
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):
            result.append([])
            for j in range(1, i+1):
                point  = self.generate_per_point(i,j)
                hash_table[(i,j)] = point
                result[i-1].append(point)
        return result
    def generate_per_point(self, i, j):
        if (j == 1) or (i == j):
            return 1
        if hash_table.get((i,j)):
            return hash_table[(i,j)]
        return self.generate_per_point(i - 1, j - 1) + self.generate_per_point(i - 1, j)
