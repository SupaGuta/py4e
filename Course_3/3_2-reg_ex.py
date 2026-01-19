import re

sample = "assets/regex_sum_42.txt"
actual = "assets/regex_sum_2358394.txt"

try:
    fh = open(actual, 'r')
except:
    print("File not found.")
    quit()

nums = list()
for line in fh:
    line.rstrip()
    fnums = re.findall('[0-9]+', line)
    if len(fnums) == 0: continue
    for fnum in fnums:
        nums.append(int(fnum))
        
print(sum(nums))

# Just for fun
print( sum( [ int(num) for num in re.findall('[0-9]+', open("assets/regex_sum_2358394.txt").read()) ] ) )