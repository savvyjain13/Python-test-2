def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
try:
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    chosen_operation = input("enter an operation (+,-,*, /)")

    if chosen_operation == "+":
        answer = add(a,b)
    if chosen_operation == "-":
        answer = subtract(a,b)
    if chosen_operation == "*":
        answer = multiply(a,b)
    if chosen_operation == "+":
        answer = divide(a,b)

except ValueError as ex:
    print("enter a valid number! Error: ",ex)
except ZeroDivisionError as ex:
    print("eyou can not divide a number by 0! Error: ",ex)
except:
    print("Enter a valid number")
else:
    print(answer)
finally:
    print("Thanks")
    #hihihihihihihihihihi
    
print("hahahahha")