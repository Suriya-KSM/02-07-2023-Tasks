#To find unique character form string

def unique_char(i):
    b=set(i)
    return len(b)
    
i="helloworld"

print("Total number of unique characters", unique_char(i))