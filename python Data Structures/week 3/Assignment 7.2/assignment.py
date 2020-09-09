fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
total = float(total)
for line in fh:
    if line.startswith('X-DSPAM-Confidence'):
        number = float(line[20:26])
        total = total + number
        count = count + 1

print('Average spam confidence:', total/count)


# # Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     print(line)
# print("Done")
