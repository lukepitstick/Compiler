i = 1
j = 1
s = 0
p = 1
n = 5
nn = 4

while (i < n):
    s += i
    p = i*p
    i += 1
    if(i%2 == 1):
        print("even!")
    while (j<nn):
        print(nn+1)
        j +=1
print("s " + str(s) + "  p " + str(p))