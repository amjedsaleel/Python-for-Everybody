# lines = input('Enter lines: ').strip().lower()
#
# words = lines.split()
# print(words)
#
# counts = dict()
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
#
# print(counts)


# # reverting lists of Keys and Values
# sample_dict = {'chuck': 1, 'fred': 42, 'jan': 100}
# print(list(sample_dict))
#
# print(sample_dict.keys())
#
# print(sample_dict.values())
#
# print(sample_dict.items())


# Two Iteration variables
sample_dict = {'chuck': 1, 'fred': 42, 'jan': 100}
for key,value in sample_dict.items():
    print(key, value)

