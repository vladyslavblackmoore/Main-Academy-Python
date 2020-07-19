"""Create any variable with name var1"""
var1 = 0
'''Check type of var1 with type function'''
print(type(var1))
'''Check is var1 is True
   Check is var1 is False'''
if var1 is True:
    print("True")
else:
    print('False')
'''Create var2 that equal to (var1 or True)'''
var2 = var1 or True
'''Check is var2 is True
   Check is var2 is False'''
if var2 is True:
    print("True")
else:
    print("False")
'''Check result for var2 and var1'''
print(f"var1 value is - {var1}\nvar2 value is - {var2}")
