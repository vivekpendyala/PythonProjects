n = int(input())
b = list(input())
g = list(input())
b = b[:n]
g = g[:n]
count = 0
for i in b:
    if i in g:
        count += 1
        g.remove(i)
    else:
        break
print(n - count)
