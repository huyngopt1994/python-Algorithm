#!/bin/python3
"https://www.hackerrank.com/challenges/simple-array-sum/problem"
import os
import sys
sys.setrecursionlimit(500001)
#
# Complete the simpleArraySum function below.
#

def simpleArraySum(ar):
    if len(ar) ==0:
        return 0
    else:
        return ar[0] + simpleArraySum(ar[1:])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
