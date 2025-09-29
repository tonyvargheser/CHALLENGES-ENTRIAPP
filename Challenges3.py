# function for whether the number is armstrong or not
def armstrong(num):
    result = 0
    l = len(str(num))
    while num>0:
        rem =num%10
        result = result + rem**l
        num =num//10
    return result
    # if num == result:
    #     return print('number is Armstrong')
    # else:
    #     return print('number is not Armstrong')

def check(a,d):
    if a == d:
        return True
    else:
        return False
        
# Main
# single number
data = int(input('Enter the number'))
r = check(data,armstrong(data))
if r == True:
    print('number is Armstrong')
else:
    print('number is not Armstrong')

# range
rag = int(input('entet the range limit'))
print('Armstrong number from 1 to',rag)
for i in range(1,rag+1):
    b = check(i,armstrong(i))
    if b == True:
        print(i, end=',')




