def Rome_To_Integer(rome):


    try:
        rome_values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        prev_values = 0
        for i in reversed(rome):
            print(i)
            values = rome_values[i]
            print(values)
            if values<prev_values:
                total -= values
            else:
                total += values
                prev_values = values
        return total
    except Exception as e:
        print("Error Ocured",e)





rom_num = input("Enter the Roman Char:").upper()
print(Rome_To_Integer(rom_num))