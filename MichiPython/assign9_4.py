fname = raw_input("Enter the fliename: ")
fhandle = open(fname)
counts = dict()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    words = line.split()
    sender = words[1]
    counts[sender] = counts.get(sender,0) +1

bigcount = None
bigword = None
#print counts.items()

for word,count in counts.items():
    if (bigcount is None) or (count > bigcount):
        bigword = word
        bigcount = count 

print bigword,bigcount


