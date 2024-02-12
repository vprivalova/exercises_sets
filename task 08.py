import itertools

subsets = []
numbers = set(int(i) for i in input().split())

for i in range(0, len(numbers)):
    subsets.extend(list((itertools.combinations(numbers, i))))

for j in range(len(subsets)):
    subsets[j] = set(subsets[j])

print(subsets)
