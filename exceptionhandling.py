a = int(input("Value of a: "))
b = int(input("Value of b: "))

try :
    print(a/b)
except Exception as err:
    print(f"Sorry an error occurred as {err}.")
else:
    print("there was no error.")
finally:
    print("i'll be executed no matter what.")
print(a+b)


# try:sxskxksxksnkxskxksmmmmmllmlsmxslsmmmmsmsmmsmsmsmsmsmxsmxxmsmxsmxsmsmsmsmsmm
#     age = int(input("input age: "))
#     if age < 18:
#         raise Exception("You must be 18+.")
#     print("Access Granted")
# except Exception as e:
#     print("Error: ",e)