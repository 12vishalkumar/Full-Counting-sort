import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the 'countSort' function below.
# The function accepts 2D_STRING_ARRAY arr as parameter.
def countSort(arr):
    # Write your code here
    d = defaultdict(list)
    L = len(arr)//2
    for i, (j,k) in enumerate(arr):
        d[int(j)].append('-' if i<L else k)
    for i in range(max(d)+1):
        for j in d[i]:
            print(j, end=' ')
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)