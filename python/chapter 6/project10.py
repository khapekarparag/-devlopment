def val(n):
    if(n==0):
        return 0
    return val(n-1)+n


print(val(5))   