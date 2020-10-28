"""
2D-List, well, they're lists inside of lists
you can use all the same methods for Lists on 2D-Lists as well,

Strucutre
example_2D_list =
            [[1,2,3],
           [4,5,6],
           [7,8,9],
           [10,11,12]]

regular_list = [1,2,3,4,5,6,7,8]

So how would you access these? well, through their index just like in regular Lists
Except its now rows and columns now
example_2D_list[rows][columns] =

regular_list[3] will get the value in the 3rd index, so = 4

So how would we get 4 out of 2D-List:?
example_2d_list[1][0]



Appending and Removing will still work the same-ish.

append will work like this:

example_2D_list.append([13,15]):
example_2D_list =
            [[1,3],
           [4,5,6],
           [7,8,9],
           [10,11,12]
           [13,15]]

remove will now require you to specifies which row,
example_2D_list[0].remove(2) will remove 2 from the "first row", which shifts 3 over.

"""
if __name__ == "__main__":
    example_2D_list = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [10, 11, 12]]
    print(example_2D_list)
    example_2D_list.append([13, 14])
    example_2D_list[4].append(15)
    print(example_2D_list)

    for number in example_2D_list:
        #print(number)



        for numbers in number:
            print(numbers)

    if 13 in example_2D_list[4]:
        print(True)

    # How would you access 5?
    print(example_2D_list[1][1])

    # lets say you want to change 5 to be 55 how would you do that?
    example_2D_list[1][1] = 55
    print(example_2D_list)

