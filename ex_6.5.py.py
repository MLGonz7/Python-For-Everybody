text = "X-DSPAM-Confidence:    0.8475"
numpos = text.find('0')
#print(numpos)

foundnum = text[numpos: ]
print(float(foundnum))