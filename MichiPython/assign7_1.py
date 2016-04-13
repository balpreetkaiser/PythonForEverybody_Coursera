fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    string = line.upper()
    print string.rstrip()

