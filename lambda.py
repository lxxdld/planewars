def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

f= lambda x:x%2==1

L1=list(filter(f,range (1,20)))
print(L1)
