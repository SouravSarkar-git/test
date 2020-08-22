last=68**815
fib = [1] * (last+1)
fib[0]=0
for i in range(2, last+1):
    fib[i] = fib[i - 1] + fib[i - 2]