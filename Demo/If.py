
#==============if -> elif -> elif -> else (verifies all following statements only if previous statement is false otherwise first if condition becomes true and give the)
A = 100
B = 90

if A*B ==100 :
 print("True")
elif A<B :
 print("False")
elif A==100:
 print("Equal")
else:
 print("newwww")
print("========================")
###=========== if -> if -> elif -> (verifies the statements )

x = 200
#z= int(input())
z = 1000

if x < z:
 print("False")
if (x>z):
 print("True")
elif (x==20):
 print("Equals to 200")
print("========================")
#==============if -> else (Compares only )

#age = int (input())
 
age = 10
if age < 20:
 print("seetha age",age)
elif age >= 20:
 print("double else")
else:
 print("age is",age)
print("========================")
#========== 

a = 10
b = 20 
if a<b or a==100:
 print("10 lesser than 20")
 print("========================")

# ================

ab = "sirija"
cd = "kasi"
print("full name") if ab == "siri" else print("not full name"+ '\n',"===========================" )

# ================

abc = 2
bcd = 330
print("A") if abc > bcd else print("B")
print("=============================")

# ================

fruit = ("apple","pineapple","Banana")
if "mango" in fruit:
 print("yes")
else:
 print("No")
 print("=============================")

# ================
