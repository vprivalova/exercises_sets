first_set = set(input().split())
second_set = set(input().split())
elem = input()
if elem in first_set.intersection(second_set):
    print("Элемент входит в пересечение множеств")
else:
    print("Элемент не входит в пересечение множеств")
