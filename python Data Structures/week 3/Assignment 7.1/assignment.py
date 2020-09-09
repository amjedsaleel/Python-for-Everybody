fname = input('Enter file name: ')

if fname.endswith('.txt'):
    pass
else:
    fname = fname + '.txt'

try:
    fh = open(fname)
except:
    print("File doest not exists")
    quit()

words = fh.read().strip()
words_upper = words.upper()
print(words_upper)