f=open("new12","r")
spe='!@#$%^&*()_+'
n=''
for i in f:
    data=i.rstrip("\n")
    for j in data:
        if j not in spe:
            n+=j
print(n)

