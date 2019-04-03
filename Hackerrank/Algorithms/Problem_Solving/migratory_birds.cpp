# Problem Statement : https://www.hackerrank.com/challenges/migratory-birds

import sys
from collections import Counter

n = int(input())
types = list(map(int, raw_input().strip().split(' ')))

birds = Counter(types)  # Counts the array into a dictionary
print(birds.most_common(1)[0][0])
