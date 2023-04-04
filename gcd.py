n = int(input())
m = [int(input()) for i in range(n)]

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

r= m[0]
for i in range(1, len(m)):
    r = gcd(r, m[i])

print(r)
