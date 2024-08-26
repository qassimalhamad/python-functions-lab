# Exercise 1: Calculate Area of a Triangle

def calculate_area_triangle(base , height):
  area = (base * height)/2

  return area

print('Exercise 1:', calculate_area_triangle(7, 3))

# Exercise 2: Calculate Simple Interest

def simple_interest(principal , rate , time):
  interest = (principal * rate * time  )/100

  return interest


print('Exercise 2:', simple_interest(1500, 3.5, 5))

# Exercise 3: Apply a Discount

def apply_discount( product_price , discout_percentage):
  discounted_price = product_price * (100-discout_percentage)/100

  return discounted_price

print('Exercise 3:', apply_discount(80, 10))

# Exercise 4: Convert Temperature

def convert_temperature (temp , unit ):
  unit.capitalize()
  if(unit == 'C'):
    convertion = (temp * 9/5) + 32
  elif(unit == 'F'):
    convertion = (temp - 32) * 5/9
  
  return convertion
print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5: Sum to N

def sum_to(n):
    total = 0
    # Start , end , step
    for i in range(1 ,  n + 1 , 1):  
        total += i  
    return total

print('Exercise 5:', sum_to(10))

# Exercise 6: Find the Largest Number


def largest( num1 , num2 , num3 ):
   if num1 >= num2 and num1 >= num3:
      return num1
   elif  num2 >= num1 and num2 >= num3:
      return num2
   else:
      return num3  

# def largest( num1 , num2 , num3 ):
#    return max(num1 , num2 , num3)
   

print('Exercise 6:', largest(10, 10, 3))

# Exercise 7: Calculate a Tip

def calculate_tip(bill , tip_percentage):
   tip = bill * (tip_percentage)/100 

   return tip

print('Exercise 7:', calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers


def product(*args):
  total = 1
  for number in args:
     total *= number
  return total

print('Exercise 8:', product(-1, 4))

# Exercise 9: Basic Calculator
#
# Create a function named `basicCalculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basicCalculator(10, 5, 'subtract') should return 5.
# basicCalculator(10, 5, 'add') should return 15.
# basicCalculator(10, 5, 'multiply') should return 50.
# basicCalculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.

def basicCalculator(num1 , num2 , operation):
   if operation == 'add':
      total = num1 + num2
      return total
   elif operation == 'subtract':
      total = num1 - num2
      return total
   elif operation == 'multiply':
      total = num1 * num2
      return total
   elif operation == 'divide':
      total = num1/num2
      return total

print('Exercise 9 Result:', basicCalculator(10, 5, "divide"))