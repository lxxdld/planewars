fpath = r'C:\Users\29652\lxx.txt'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

with open(fpath,'a') as f:
	f.write('lxx num1')
