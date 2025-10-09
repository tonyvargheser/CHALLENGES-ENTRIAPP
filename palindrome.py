def palindrome(num):
    if num<0:
        return False
    orginal_num = num
    reverse_number =0
    while num>0:
        digit = num%10
        reverse_number= reverse_number*10+digit
        num =num//10
    return orginal_num == reverse_number



number = int(input("Enrer the number:   "))
print(palindrome(number))