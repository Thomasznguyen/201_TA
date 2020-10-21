if __name__ == "__main__":
    key = ""
    section62 = {}
    # Will keep going until stop is hitted
    while key != "STOP":
        # getting in our name
        key = input("What would you like the person name to be?(STOP to stop): ")

        # checking if the name is STOP,
        if key != "STOP":
            studentdict = {}
            value = input("what would you like the person role to be?: ")
            # add value to the studentdict with key of "Role
            studentdict["Role"] = value

            # Checking to see if the key already exists inside the main dict
            if key not in section62:
                section62[key] = studentdict
            else:
                # Error Message
                print(key, " is already in section62")
                # F string format, basically quicker version of above.
                print(f"{key} is already in section62")
            # another example of adding values to the secondary dict.
            grade = input("what is the grade?")
            #studentdict["Role"] = grade
            # adding grades to key of "grade", no need to add it again to section62 dict
            studentdict["grade"] = grade

            # as long as we dont leave the while loop, then studentdict can be changed
            # without needing to be reassign
    #accessing section62 dict is just like 2d- list
                    #key for section 62
                            #key for studentdict
    print(section62["tommy"]["Role"])
    print(section62.keys())
    print(section62.values())

