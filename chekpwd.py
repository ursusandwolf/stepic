p = input()
def check_password(p):
    easy = False
    if len(p) < 10 or \
            len([d for d in p if d.isdigit()]) < 3 or\
            len([c for c in p if c in "!@#$%*"]) < 1 or\
            len([c for c in p if c.isupper()]) < 1:
        easy = True
    print("Easy peasy" if easy else "Perfect password")

check_password(p)
