pref = set(input().split())
n = int(input())
all_friends_pref = set()
result = set()

for i in range(n):
    friend_pref = input().split()
    all_friends_pref.update(friend_pref)

for elem in pref:
    if elem not in all_friends_pref:
        result.add(elem)

print(len(result))
