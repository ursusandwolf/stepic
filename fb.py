n = int(input())

def generate_fizz_buzz_list(n):
    l = list()
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            l.append("FizzBuzz")
        elif i%3 == 0:
            l.append("Fizz")
        elif i%5 == 0:
            l.append("Buzz")
        else:
            l.append(i)

    return l


print(generate_fizz_buzz_list(n))
