# 4th program
a, b = 13.42, 42.13
print(a, b)
aint, bint = int(a), int(b)
print(aint, bint)
afl, bfl = int((a - aint) * 100), int((b - bint) * 100)
print(afl, bfl)
print(aint == bfl or bint == afl)
