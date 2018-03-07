try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 while denominator == 0:
     print('Cannot divide by 0, please input another value')
     denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
 print(fraction)
except ValueError:
 print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
 print("Cannot divide by zero!")
print("Finished.")

'''1.
      A ValueError will occur when an argument is input that is not of the correct type
   For example the type has to be a int or a float'''

'''2.
      A ZeroDivision error will occur whenever python tries to execute a fraction
      with a 0 in the denominator as it is undefined.'''


