#Removing Vowels from string

def final(string1):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    output="" 
    for i in range (len(string1)):
        if string1[i] not in vowels:
            output = output + string1[i]
    return output


string1='Welcome to Automation Testing'




print("Result after removing vowels is :", final(string1))