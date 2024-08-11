# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        npos = line.find('0')
        fnumb = float(line[npos:])
        count = count + 1
        total = total + fnumb

average = total/count    
print("Average spam confidence:", average)
