import itertools

numbers = set(int(i) for i in input().split())

transpositions = set(itertools.permutations(numbers))
sorted_transpositions = sorted(list(transpositions))

print(sorted_transpositions)
