name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

sender = dict()
for line in handle:
    if line.startswith('From:'):
        line = line.split()
        word = line[1]
        sender[word] = sender.get(word, 0) + 1

bigword = None
bigcount = None
for word, count in sender.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)