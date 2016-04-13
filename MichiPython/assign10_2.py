name = raw_input("Enter the filename: ")
if len(name)<1:
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print "File not found!!!"
    exit()

counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    words = words[5]
    words = words.split(':')
    words = words[0]
    counts[words] = counts.get(words,0)+1
    
result = counts.items()
result.sort()
for k,v in result:
    print k,v	
