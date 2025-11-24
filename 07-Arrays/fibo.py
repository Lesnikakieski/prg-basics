def f(n):
    vals=[0,1]
    for i in range(2,n):
        vals.append((vals[i-1]+vals[i-2]))
    return vals[-1]


print(f(9))

