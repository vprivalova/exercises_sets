import itertools

subsets = []
numbers = set(int(i) for i in input().split())
capacity = int(input())

subsets = list((itertools.combinations(numbers, capacity)))
for i in range(len(subsets)):
    subsets[i] = set(subsets[i])

print(subsets)
