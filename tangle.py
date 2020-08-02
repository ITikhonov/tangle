from sys import argv
f=open(argv[1])
m={'stdout':[]}
cm=m['stdout']
empty=True
text=True
while True:
	l=f.readline()
	if l=='': break
	prev_empty=empty
	empty=False
	prev_text=text
	text=False
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
	elif l.strip()=='':
		empty=True
	else:
		text=True
		if (not prev_empty) and (not prev_text):
			print('WARNING! This line probably should be code or have a blank line above:')
			print(l)
	if not empty and (prev_text and (not prev_empty) and (not text)):
		print('WARNING! Line before that probably should be code or have a blank line after:')
		print(l)
def e(x,i=''):
	if type(x) is tuple: return e(m[x[0].split()[0]],i+x[1])
	if type(x) is list: return ''.join([e(y,i) for y in x])
	return i+x
for x,y in m.items():
	if x.startswith('>'): open(x[1:],'w').write(e(y))
