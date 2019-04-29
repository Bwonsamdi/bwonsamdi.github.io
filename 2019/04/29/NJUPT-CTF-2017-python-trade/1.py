import base64

def encode(message):
    s = ''
    for i in message:
        x = ord(i) ^ 32
        x = x + 16
        s += chr(x)

    return base64.b64encode(s)
    
correct = 'XlNkVmtUI1MgXWBZXCFeKY+AaXNt'
ss = ''
cor = base64.b64decode(correct)
for i in cor:
    y = int(i) - 16
    y ^= 32
    ss += chr(y)

print (ss)