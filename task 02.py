n = int(input())
overall_courses = set()

for i in range(n):
    courses = input().split()
    overall_courses.update(courses)

print(len(overall_courses))
