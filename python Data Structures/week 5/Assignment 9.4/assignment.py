name = input("Enter file: ")
handle = open(name)

mails = list()
for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        mail = words[1]
        mails.append(mail)

count = dict()
for mail in mails:
    count[mail] = count.get(mail, 0) + 1

largest = 0
for key, value in count.items():
    if value > largest:
        largest = value
        largest_mail_messages = key

print(largest_mail_messages, largest)


