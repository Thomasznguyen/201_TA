"""
Today we are going over while loops.
-We've gone over for loops already which are basically loops
that will iterate a set amount of times.

While loops will iterate through stuff until a condition is false.

Structure:
while (Condition): < > <= >=  == !=
    blah
    blah
    blah

the "Blahs" is indented under the while loops and will continue to run
for as long as the condition is true.


so While loops use booleans conditions
Condition = True
            then the body of the while loops (blahs) will be executed

Condition = False
            Then the body of the while loops(blahs) are skipped

"""
#Example:
date = 0;
#I want date to be between 1 and 10

while date < 1 or date > 10:
    date = int(input("Enter the day: "))
print("Today is September",date)

#So what is this good for?

"""
test = "blah"
while test != "string":
    test = input("enter a string")

print(test)

"""

#Sentinel Values

list_names = []
sentinel_string = "quit"
names = "blah"
while names != sentinel_string:
    names = input("Enter a Name: ")
    if names != sentinel_string:
        list_names.append(names)

print(list_names)