# for each loops
# loops through the list itself and gets the elements within it.

# Structure:   for (variable) in (list):
example_list = [54,34,38,75,23,987]

# you are basically assigning the elements inside the list Example List, to the variable (numbers)
for numbers in example_list:
    print(numbers) # this will print out every "number" inside the list


# for i loops (i = index)
# loops through an integer using range(start,end). to loop through list index
# you can use range(len(list)) the len() will get the length of the list,
# range will output a int from 0 (if no start is provided) to the len of that list\
# useful for going through every index value of a list

# structure: for (i) in range(len(list)):
print("------------------------------------------")
for i in range(len(example_list)):
    # this will print out using the list's index from 0, to (len(list) - 1)
    #print(example_list[i])

    # you can change the value of the lists too,
    # this will take the elements at the given index and add 1 to it,
    # so 54 will become 55 after this step.
    example_list[i] = example_list[i] + 1
    print(example_list[i])



