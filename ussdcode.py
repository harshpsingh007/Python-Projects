def gsm7bitdecode(f):
   f = ''.join(["{0:08b}".format(int(f[i:i+2], 16)) for i in range(0, len(f), 2)][::-1])
   return ''.join([chr(int(f[::-1][i:i+7][::-1], 2)) for i in range(0, len(f), 7)])
code = input("Enter the code")
print(gsm7bitdecode(code))
