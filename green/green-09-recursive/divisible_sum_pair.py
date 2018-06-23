#!/bin/python3
"https://www.hackerrank.com/challenges/divisible-sum-pairs/problem"

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    """
    :param n:
    :param k:
    :param ar:
    :return:
    """
    # Requirement: find i, j i<j: a[i]+ a[j] % k
    # Base case
    if len(ar) <2:
        return 0
    # Recursive case
    count = 0
    for i in ar[1:]:
        if (ar[0] +i) % k ==0:
            count +=1
    return count + divisibleSumPairs(n,k,ar[1:])

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)
