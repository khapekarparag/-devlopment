def bob(n):
    if (n==0):
        return
    print(n)
    bob(n-1)

bob(10)
