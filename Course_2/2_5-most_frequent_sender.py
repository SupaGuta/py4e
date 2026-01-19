fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "assets/mbox-short.txt"

fh = open(fname)

senders = dict()

for line in fh:
    if not line.startswith('From '):
        continue
    
    line.rstrip()
    words = line.split()
    sender = words[1]
    senders[sender] = senders.get(sender, 0) + 1

sender_address = None
sender_count = None

for key, value in senders.items():
    if sender_count is None or value > sender_count:
        sender_address = key
        sender_count = value

print(sender_address, sender_count)