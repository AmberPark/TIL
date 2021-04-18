def fibo(n):
    value = [0, 1]
    if n < 2:
        return value[n]
    else:
        for i in range(2, n+1):
            value.append(value[i-2]+value[i-1])
        return value[n]
print(fibo(10))

# 얘도 시간복잡도 O(n)