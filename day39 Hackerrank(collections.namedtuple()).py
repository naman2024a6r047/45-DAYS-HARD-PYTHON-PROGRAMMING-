from collections import namedtuple

n = int(input())

Student = namedtuple('Student', input().split())

total_marks = sum(int(Student(*input().split()).MARKS) for _ in range(n))

print(f"{total_marks / n:.2f}")
