n = int(input())
total = set()
for n in range(n):
    line = list(map(int, input().split()))
    total.update(line)

print(total)
print(len(total))
