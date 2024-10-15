n = int(input('Digite um valor:\n'))
t1 = 0
t2 = 1
count = 3
print('-'*10)
print(t1)
print(t2)
while count <=n:
    t3 = t1+t2
    print(t3)
    t1=t2
    t2=t3
    count +=1

