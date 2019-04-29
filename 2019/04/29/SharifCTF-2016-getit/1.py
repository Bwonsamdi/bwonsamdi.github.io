s = 'c61b68366edeb7bdce3c6820314b7498'
ss = ''
for i in range(len(s)):
    if i & 1 :
        v = 1
    else :
        v = -1
    x = ord(s[i]) + v
    ss += chr(x)
print(ss)