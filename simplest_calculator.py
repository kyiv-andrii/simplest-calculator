#!/usr/bin/env python3

# simplest_calculator.py
# author Andrii Onopriienko
# It's my first program on Python

print()

# Input first number
# Потрібно буде спробувати loop для перевірки, чи дійсно введено числове значення.
print('Enter first number, please:')
inputA = input()  #print(type(inputA)) # <class 'str'>
print()
a = float(inputA)  #print(type(a)) # <class 'float'>

# Input operator
print('''Enter one of operators, please:
    (addition)          +
    (subtraction)       -
    (multiplication)    *
    (division)          /
    (modulus)           %
    (floor division)    //
    (exponentiation)    **
''')
operator = input()  #print(type(operator)) # <class 'str'>

# Input second number
print()
print('Enter second number, please:')
inputB = input()  #print(type(inputB)) # <class 'str'>
print()
if (operator == "/" and inputB == '0'):
  print('Division by ZERO is impossible. Enter another number, please:')
  inputB = input()
  print('Let us compute!\n')
  print()
elif (operator == "%" and inputB == '0'):
  print('Division by ZERO is impossible. Enter another number, please:')
  inputB = input()
  print('Let us compute!\n')
  print()
elif (operator == "//" and inputB == '0'):
  print('Division by ZERO is impossible. Enter another number, please:')
  inputB = input()
  print('Let us compute!\n')
  print()
else:
  print('Let us compute!\n')

b = float(inputB)  #print(type(b)) # <class 'float'>

# Computing the result
if operator == '+' :
  print('Result of Addition is:')
  print(str(a) + ' ' + (operator) + ' ' + str(b) + ' = ' + str(a + b))
elif operator == '-' :
  print('Result of Subtraction is:')
  print(str(a) + ' ' + (operator) + ' ' + str(b) + ' = ' + str(a - b))
elif operator == '*' :
  print('Result of Multiplication is:')
  print(str(a) + ' ' + (operator) + ' ' + str(b) + ' = ' + str(a * b))
elif operator == '/' :
  print('Result of Division is:')
  print(str(a) + ' ' + (operator) + ' ' + str(b) + ' = ' + str(a / b))
elif operator == '%' :
  print('Remainder is:')
  print(str(a) + ' ' + (operator) + ' ' + str(b) + ' = ' + str(a % b))
elif operator == '//' :
  print('Result of Floor Division is:')
  print(str(a) + ' ' + (operator) + ' ' + str(b) + ' = ' + str(a // b))
  print('            ( and Remainder is: ' + str(a % b) + ' )')
elif operator == '**' :
  print('Result of Exponentiation is:')
  print(str(a) + ' ' + (operator) + ' ' + str(b) + ' = ' + str(a ** b))
else:
  print('Sorry. You have a mistake with input. Good luck!')
