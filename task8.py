

# function to check if two strings are anagram or not
 
def anag(str1, str2):
     
    
    if(sorted(str1)== sorted(str2)):
        print("True") 
    else:
        print("False")
         
 
str1 ="are"
str2 ="ear"
anag(str1, str2)