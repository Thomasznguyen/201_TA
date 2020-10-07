if __name__ == "__main__":
    sampleString = "Sean Jordan"
    # .upper will make the string into all lowercase
    print(sampleString.upper())

    # .lower will make the string into all lowercase
    print(sampleString.lower())

    # len() will return the length of the string
    print(len(sampleString))

    # This is called String concatenation, It will join two strings together
    newstring = sampleString + " is the head TA"
    print(newstring)

    blahstring = ""
    liststring = ["a","b","c","d"]
    for item in liststring:
        blahstring = blahstring + item
    print(blahstring)


    # .strip will take out the whitespace from the beginning and end
    sentence = "\t\tThis is a sample sentence.\n\n"
    sentence = sentence.strip()
    print(sentence)

    #.split will make a list of substrings after removing whats inside the ()
    testString = "This is a test string"
    testString = testString.split()
    print(testString)


    testParaString = "This#is#a#test#String"
    testParaString = testParaString.split("#")
    print(testParaString)

    #join will take a list of strings and concatenate/join them together
    stringList = ["Hello","my","name","is","Tommy","your midterm is today"]
    newStringList = " ".join(stringList)
    print(newStringList)