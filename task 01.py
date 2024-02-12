numbers = [int(i) for i in input().split()]
n = int(input())
repeats = set()

for elem in numbers:
    if numbers.count(elem) > 1:
        repeats.add(elem)

if n in repeats:
    print("Входит в множество повторяющихся чисел")
else:
    print("Не входит в множество повторяющихся чисел")
