##### ASSIGNMENT STARTS HERE #####


#%%
# FOR ALL ASSIGNMENTS: I used the end parameter so the output and label appear as a single line, 
# For assignments 2 and 3: the 'float' is there to accommodate for decimals
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''
year1 = int(input("Enter the earlier year: "))
year2 = int(input("Enter the later year: "))

difference = (year2 - year1)

print("Year 1:", year1)
print("Year 2:", year2)
print("Difference:", difference)

#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''
#The Celsius output is determined by input in Fahrenheit

print('Fahrenheit:', end=" ")
Fahrenheit = input()
print('Celsius:', end=" ")
Fahrenheit = float(Fahrenheit)
print((Fahrenheit - 32) * 5 / 9)

#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''
print('USD:', end=" ")
USD = input()
print('EU:', end=" ")
USD = float(USD)
print(USD * 0.97)

##### ASSIGNMENT ENDS HERE #####
