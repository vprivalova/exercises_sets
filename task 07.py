import itertools

numbers = set(int(i) for i in input().split())

sorted_numbers = sorted(list(numbers))
transpositions = set(itertools.permutations(sorted_numbers))
sorted_transpositions = sorted(list(transpositions))

print(sorted_transpositions)
