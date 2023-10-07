#To find the most frequent character in the string

def FreqChar(str):

    mp = {}
    n = len(str)
    ans = ''
    cnt = 0
 
    for i in range(n):
        if str[i] in mp:
            mp[str[i]] += 1
        else:
            mp[str[i]] = 1
 
        if cnt < mp[str[i]]:
            ans = str[i]
            cnt = mp[str[i]]
 
    return ans

str = "Welcome to Automation Testing"
print("Most frequrnt character is:", FreqChar(str))