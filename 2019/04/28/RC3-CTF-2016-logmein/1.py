a = ':\"AL_RT^L*.?+6/46'
b = 'harambe'
key = ''
for i in range(len(a)):
    m = ord(a[i]) ^ ord(b[i % 7])
    key += chr(m)
print(key)