#Print hello world in python!
print("Hello world")

#Getting inputs from the user:

#Getting our first number from the user (no1):
no1 = int(input('In put your first number here: ', ))
#Getting our second number from the user (no2):
no2 = int(input('In put your second number here: '))

#Setting the simple functions of a calculator and getting what type of mathematical operation should be performed

print("These are the operations available: press the '+' key if you want to add your first and second number, press the '-' key if you want to subtract number 1 and number 2, press the '*' key if you want to multiple your first number and second number, if you want to divide number 1 and number 2 press the '/' key")

#Getting the input statement for what operation is desired by the User

op = input('input your desired operation over here:', )


#Solving the actual eqations with the desired input


#Creating the if statement for the addition function
if op == '+':
  print(no1 + no2)

elif op == '-':
  print(no1 - no2)

elif op == '*':
  print(no1 * no2)

elif op == '/':
  print(no1 / no2)

else:
  print("You didn't add an elgible operation symbol")
