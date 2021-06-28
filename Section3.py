# This file contains executable samples from section 3 of the python course
# Covers - some basic functions such as print
# Covers - data types - int and string
# Covers - basic operations
# Covers - string manipulation and type conversion

# First scenario - hello world
theString = "Hello World"
print(theString)

#Second scenario - concatenation
thefirstString = "Hello"
theSecondString = "World"
print(thefirstString + " " + theSecondString)

#Second and a half - input
#print(input("Enter a value")) <- uncomment to try

#Third scenario - special characters
print("this escapes a backslash with a \\")
print("This escapes a \" with a \\")
print("This adds a \\n \n to print to a second line")

#Fourth Scenario - Math Operations
numberOne = 2
numberTwo = 4
print("adding")
print (numberOne + numberTwo)
print("subtracting")
print (numberOne - numberTwo)
print("Multiplying")
print (numberOne * numberTwo)
print("Dividing")
print (numberOne / numberTwo)
print("Modulus")
print (numberOne % numberTwo)
print("Exponential")
print (numberOne ** numberTwo)
print("floor")
print (numberOne // numberTwo)

print("In this example, the numbers are converted to strings prior to the operation, resulting in concatenation " + str(numberOne) + str(numberTwo))

print("In this example, the numbers are converted after addition " + str(numberOne + numberTwo))

#Fifth Scenario - data types
anInteger = int(9)
print("this is an integer " + str(anInteger))

afloat = float(9)
print("this is a float " + str(afloat))

#complex data types
alist = list(("Value1","Value2", "Value3"))
for i in alist:
    print(i)
print(type(alist))

# List items are ordered, changeable, and allow duplicate values.
# The data type can be defined as a list using square brackets

aTuple = tuple(("value4","value5","value6"))
for i2 in aTuple:
    print(i2)
print(type(aTuple))

# A tuple is a collection which is ordered and unchangeable.
# The data type can be defined as a tuple using round brackets

aSet = set(("value7","value8","value9"))
for i3 in aSet:
    print(i3)
print(type(aSet))

# A set is a collection which is both unordered and unindexed.
# The data type can be defined as a set using curley braces

theDict = {
    "brand":"jeep",
    "model":"wrangler"
}
print(theDict["brand"])
print(type(theDict))

Sixth Scenario - string formatting
aNumber = 10
print("This is the number " + aNumber) 