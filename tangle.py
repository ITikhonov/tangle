from sys import argv,stdout
cf=stdout
f=open(argv[1])
while True:
	l=f.readline()
	if l=='': break
	if l.startswith('-'):
		cf.write(l[1:])
	elif l.startswith('='):
		if cf!=stdout: cf.close()
		cf=open(l[1:].strip(),'w')
	elif l.startswith('+'):
		if cf!=stdout: cf.close()
		cf=open(l[1:].strip(),'a')
