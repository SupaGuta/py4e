fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "assets/mbox-short.txt"

fh = open(fname)

hours = dict()

for line in fh:
    if not line.startswith('From '):
        continue
    
    line.rstrip()
    time = line.split()[5]
    hour = time.split(':')[0]
    hours[hour] = hours.get(hour, 0) + 1

sort_hours = sorted(hours.items())
for (k, v) in sort_hours :
    print(k, v)