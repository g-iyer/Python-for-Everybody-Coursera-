name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
email=dict()
handle = open(name)
for line in handle:
    if line == '':continue
    else:
        line.rstrip()
        if line.startswith('From '):
			words = line.split()
			#print words
			eml = words[1]
			#print eml
			email[eml] = email.get(eml,0) + 1            
eml_val =None
eml_count = None
for eml,val in email.items():
	if eml_val == None or val > eml_count:
		eml_val = eml
		eml_count = val
print eml_val,eml_count
#print email