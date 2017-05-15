# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for lin in fh:
    lin_s=lin.rstrip()
    lin_u = lin_s.upper()
    print lin_u