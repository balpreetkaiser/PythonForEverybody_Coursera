fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    inter_line = line.rstrip()
    words = inter_line.split()
    for word in words:
        if word in lst:
           continue
        lst.append(word)

lst.sort()
print lst
