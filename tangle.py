from sys import argv
f=open(argv[1])
m={'stdout':[]}
cm=m['stdout']
while True:
	l=f.readline()
	if l=='': break
	if l.startswith('-'):
		cm.append(l[1:])
	elif l.startswith('='):
		name=l[1:].strip()
		cm=m.get(name)
		if not cm:
			cm=[]
			m[name]=cm
	elif l.startswith('>'):
		cm.append((l[1:].strip(),))
def e(x):
	if type(x) is tuple: return e(m[x[0]])
	if type(x) is list: return ''.join([e(y) for y in x])
	return x
for x,y in m.items():
	if x.startswith('>'): open(x[1:],'w').write(e(y))
