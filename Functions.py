"""
Functions, What are they?

Well, Functions are basically chunks of code that does one specific thing
For Example, lets say you want to know the greatest of two number.

Before you would do:
if number1 > number2:
    print(f"{number1} is greater")
else:
    print(f"{number2} is greater")

and you would have to do this every single time you want to know which one is greater

Functions will basically allow you to "call" it and it will perform a the code inside it's block
and return something.
so lets say that if-else statement, if you were to put that inside a function called higher() you can then just call
higher() whenever you want to know whats higher.

Function structure would look like this:

def functionName(parameters):
    function body
    ...
    (optional)- return


so our function would look like:
"""


# This function is called higher, it takes in two parameters, number1 and number2
def higher(number1, number2):
    # compare number1 vs number2
    if number1 > number2:
        # returns a number
        return number1
    else:
        return number2


def print_numbers(number1, number2):
    highest_number = higher(number1, number2)
    print(f"The highest number is {highest_number}")


def print_name(name):
    print(f"Hello!, my name is {name}")


if __name__ == "__main__":
    print(higher(1, 2))

    firstNumber = int(input("First Number: "))
    secondNumber = int(input("second Number: "))
    print_numbers(firstNumber, secondNumber)

    # name = input("what is your name?")
    # print_name(name)
