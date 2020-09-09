file_name = input('Enter file name: ')

if file_name.endswith('.txt'):
    pass
else:
    file_name = file_name + '.txt'

try:
    files = open(file_name)
except:
    print('File not exists, Please try agin!!!')
    quit()

count = 0
for line in files:
    line = line.rstrip()
    count += 1
print('Total lines:', count)

