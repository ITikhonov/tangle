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
		n=l[1:]
		cm.append((n.strip(),n[:-len(n.lstrip())]))
def e(x,i=''):
	if type(x) is tuple: return e(m[x[0]],x[1])
	if type(x) is list: return ''.join([e(y,i) for y in x])
	return i+x
for x,y in m.items():
	if x.startswith('>'): open(x[1:],'w').write(e(y))
