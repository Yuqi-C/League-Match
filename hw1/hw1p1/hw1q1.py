import sys

def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)    

def anagrams(input):

    length = len(input)
    freq = [0] * 26
    for i in range(0, length):
        if(input[i] >= 'a' and input[i] <= 'z'):
            freq[input[i]-'a'] = freq[input[i]-'a'] + 1;
        else if(input[i] >= 'A' and input[i] <= 'Z'):
            freq[input[i]-'A'] = freq[input[i]-'A'] + 1;    
        else:
            return 0
    
    res = 1
    for element in freq
        res = res * factorial(element)

    return factorial(length) // res

input = sys.argv[1]
if input == '':
    print("empty")
else:
    ret = anagrams(input)
    if ret == 0:
        sys.sederr.write("invalid")
    else:
        print(ret)            


