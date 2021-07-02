h, m = map(int, input().split())
if 0 < h and m < 45:
    print(h-1, end=' ')
    print(m+15)
elif 0<h and m>=45:
    print(h, end=' ')
    print(m-45)
elif h == 0 and m < 45:
    print(23, end=' ')
    print(m+15)
else:
    print(h, end=' ')
    print(m-45)