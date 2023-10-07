#To find the given string is Palindrome or not.

def palindrome(string):
    for i in range(0, int(len(string)/2)):
        if string [i] != string [len (string) -i-1]:
            return False
        else:
            return True
string=input("Enter the string you want to check it is a plaindrome or not:")
print (palindrome(string))
