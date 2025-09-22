print(" 1. English \n 2. History \n 3. Maths \n 4. Malayalam")
e = 0
h = 0
mat = 0
mal = 0
count = 1
for count in range(1,10):
    if e==0 or h==0 or mat==0 or mal==0:
        b = int(input("Please select your subject:-"))
        if b ==1:
            if(e<=0):
                e =float(input("Enter the Marks for English:"))
            else:
                print("English Mark is already assigned,Can\'t do the Modification, please Contact Admin or choose another subject")
        elif b==2:
            if(h<=0):
                h =float(input("Enter the Marks for History:"))
            else:
                print("History Mark is already assigned,Can\'t do the Modification, please Contact Admin or choose another subject")

        elif b==3:
            if(mat<=0):
                mat =float(input("Enter the Marks for Maths:"))
            else:
                print("Maths Mark is already assigned,Can\'t do the Modification, please Contact Admin or choose another subject")
        elif b==4:
            if(mal<=0):
                mal =float(input("Enter the Marks for Malayalam:"))
            else:
                print("Malayalam Mark is already assigned,Can\'t do the Modification, please Contact Admin or choose another subject")
    else:
        break
print(" English :",e,"\n","History :",h,"\n","Maths :",mat,"\n","Malayalam :",mal)
p = input("please calculate the final result:")
total = e+h+mat+mal
percentage= total/400*100
print("Total marks   =",total)
print("Percentage  =",percentage)
if percentage>=90:
    print("Garde   = A+     :Pass")
elif percentage>=80 and percentage<90:
    print("Garde   = A      :Pass")
elif percentage>=70 and percentage<80:
    print("Garde   = B+    :Pass")
elif percentage>=60 and percentage<70:
    print("Garde   = B     :Pass")
elif percentage>=50 and percentage<60:
    print("Garde   = C+    :Pass")
elif percentage>=40 and percentage<50:
    print("Garde   = C    :Pass")
elif percentage>=30 and percentage<40:
    print("Garde   = D+    : FAIL")
    


    












        



   
   
    

