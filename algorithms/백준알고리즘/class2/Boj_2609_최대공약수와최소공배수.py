a, b = map(int, input().split())

a_g = []
b_g = []

for i in range(1, a+1):
    if a % i == 0:
        a_g.append(i)
for i in range(1, b+1):
    if b % i == 0:
        b_g.append(i)
gcf_lst = []
for a in a_g:
    for b in b_g:
        if a == b:
            gcf_lst.append(a)

gcf = max(gcf_lst)


lcm = (a // gcf) * (b // gcf) * gcf

print(gcf)
print(lcm)