n = input()
odd = [int(n[i])*2 for i in range(-2,-17,-2)]
even = [int(n[i]) for i in range(-1,-17,-2)]
total = 0
for d in odd:
    if d <= 9:
        total +=d
    else:
        total += d - 9
for d in even:
    total +=d

print(total%10==0)
