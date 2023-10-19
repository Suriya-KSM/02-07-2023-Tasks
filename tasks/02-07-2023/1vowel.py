#Python program to calculate the total number of vowels and count of each vowel.

__a__= 'Guvi Geeks Network Private Limited'
__a__=__a__.casefold()

vowel=0

b='aeiou'
count={}.fromkeys(b, 0)

for i in __a__:

    if i in count:
        count[i]+=1

    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowel = vowel+1



print ("Total number of vowels in the string is ", vowel) 
print('Total number of each Vowel',count)
