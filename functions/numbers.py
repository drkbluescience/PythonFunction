# Strong Number
# A number whose sum of all digits factorial is equal to the number itself
# eg 145 = 1! + 4! + 5!
#        = 1*1 + 4*3*2*1 + 5*4*3*2*1
#        = 1 + 24 + 120
#        = 145

# function to calculate factorial
def factorial(digit):
  if digit == 0 or digit == 1:
    return 1
  return digit * factorial(digit - 1)

#function to check strong number
def check_strong(num):
  check_num = num
  sum_of_digits = 0

  while check_num > 0 :
    digit = check_num % 10
    sum_of_digits += factorial(digit)
    check_num = check_num // 10

  if sum_of_digits == num:
    return f"{num} is a Strong Number"
  else:
    return f"{num} is not a Strong Number"



# Neon Number
# Numbers where sum of digits of the square of number is equal to number
# ex 9
# square of 9 = 9*9 = 81
# sum of digits of 81 = 8 + 1 = 9

def show_neon(num):

  # Square of number
  square_of_num = num ** 2
  digits_sum = 0

  while square_of_num != 0:
    digits_sum = digits_sum + square_of_num % 10
    square_of_num = square_of_num // 10

  if digits_sum == num:
    return f"{num} is a Neon Number"
  else:
    return f"{num} is not a Neon Number"



# Fibonacci Number
# Start with two 1s and add these together to get the next number. 
# Each time adding the last two numbers created in order to get the next one.
# This gives us the list of Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

def fibonacci(num):
   
  # Check if input is 0 then it will
  # print incorrect input

  # if num < 0:
    # print("Incorrect input")
 
  # Check if n is 0
  # then it will return 0
  elif num == 0:
    return 0
 
  # Check if n is 1,2
  # it will return 1
  elif num == 1 or num == 2:
    return 1
 
  else:
    return fibonacci(num-1) + fibonacci(num-2)



# Perfect Numbers
# A perfect number is a positive integer that is equal to the sum of its factors (not including itself).
# The factors of 4 are 1, 2 and 4 (these are the numbers that divide exactly into 4)
# So if we add these together, not including 4 itself, we get 1 + 2 = 3, hence 4 is not a perfect number.
# The smallest perfect number is 6. Its factors are 1, 2, 3 and 6. The sum of these is 1 + 2 + 3 = 6, hence 6 is perfect.

def perfect_number(num):
  sum = 0
  for i in range(1, num):
    if(num % i == 0):
      sum = sum + i

  if (sum == num):
    return f"{num} is a Perfect Number"
  else:
    return f"{num} is not a Perfect Number"