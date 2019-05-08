name = input('name: ')
num = len(name) * 0x17cfb + ord(name[0])
print('key is: AKA-'+str(num))
