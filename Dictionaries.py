"""
Dictionaries are a store device in python that allows you
to store data as keys and values,

you would then search for these values, using the keys just like in a list.
in Lists you would use indexes to search for your item.

Structure of dictionary:

dictionaryName = {"key":"value"}
Keys can be any data types that are immutable: #not changeable
    bool,int,string,char
Values have no restriction, that means that they can be lists, or even
dictionaries themselves.

To access a dictionary you would use its key the same as a List

so to get "value" out of dictionaryName you would do:
print dictionaryName["key"] # this would print out value

you can also iterate through a dictionary:
for keys in dictionaryName:
    print(keys) # this would print out the keys
    print(dictionaryName[keys]) # this would loop through
                                # the dictionary and pull out the values

to add to a dictionary you can just assign it:
dictionaryName["blah"] = "hello" # here we assigned the key="blah" and the value of "hello"

the .get() method will allow us to pull out a value from a dictionary using the key,
and if its not there just returns none or a value.

example: print(dictionaryName.get("key","error message"):
# this will try to find a key="key" if it cant find it then it'll print out the "error message"

you can also search for keys inside a dictionary using if... in statement
so:     if "key" in dictionaryName:
            print("yes its here")


to delete keys you would use the del keyword:
del dictionaryName["key"]

.keys() and .values() will return a list with all the keys and or values

"""
if __name__ == "__main__":
    section62 = {"Tommy": "TA",
                 "Malcolm": "Student",
                 "Kyler": "Student",
                 "Meseret": "Student"
                 }
    print(section62)
    print(section62["Kyler"])

    section62["new student"] = "Student"
    print(section62)

    #print(section62["bob"]) #Key Error.
    print(section62.get("bob", "Person not found")) #Key, Error Message



    if "Meseret" in section62:
        print("Meseret is here!")
    else:
        print("Nope")

    del section62["Meseret"]

    if "Meseret" in section62:
        print("Meseret is here!")
    else:
        print("Nope")

    key = (section62.keys())
    values = (section62.values())
    print(key)
    print(values)
