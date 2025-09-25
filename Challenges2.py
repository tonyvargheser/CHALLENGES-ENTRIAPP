num = []
even = []
odd = []
dividby5_3 = []
for i in range(1,51,1):
    num.append(i)
print(num)
for i in num:
    if i%2==0:
        even.append(i)
        
    else:
        odd.append(i)
print()    
print(even)
print()
print(odd)
for i in num:
    if i%5==0 and i%3==0:
        dividby5_3.append(i)

print(dividby5_3)