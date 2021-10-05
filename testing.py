#This program will check if the year entered by the user is a leap year or not.

year = input("Enter year: ")

""" 
The variable below checks that is the year divisible by four
because a leap year occurs every 4 years which
means that a leap year is divisible by four
"""
check = year%4

# The below if and elif statements check that the year when divided by 4 gives a remainder or not
try:
      if check == 0:
            print("The year is a leap year")
      elif check != 0:
            print("The year is not a leap year")
except ValueError:
      print("Huh? Big FOOL, don't you know that a year has number only?") #For fools