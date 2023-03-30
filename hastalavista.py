n = input().lower().split(',')
s = set()
previous = 0

for x in n:
    s.add(x)
    print(len(s)==previous)
    previous = len(s)
