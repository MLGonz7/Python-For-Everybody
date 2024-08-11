name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hours = time[:2]
        counts[hours] = counts.get(hours, 0) + 1

for key,val in sorted(counts.items()):
    print(key,val)