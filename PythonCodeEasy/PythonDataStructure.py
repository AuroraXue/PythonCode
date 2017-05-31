# fname = raw_input("Enter file name: ")
# fh = open(fname)
# x=list()
#
# for line in fh:
#     line=line.rstrip()
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     start=line.find('.')-1
#     numString=line[start:]
#     x=x+numString
#
#
# x=map(float,x)
# ave= sum(x)/len(x)
# print "Average spam confidence:",ave

# fname = raw_input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
# fh = open(fname)
# count = 0
# for line in fh:
#     if line.startswith('From:'):
#         count = count + 1
#         line=line.strip()
#         words=line.split()
#         print words[1]
#
#
# print "There were", count, "lines in the file with From as the first word"

# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# people=dict()
# for line in handle:
#     if line.startswith('From:'):
#         words=line.split()
#         name=words[1]
#         people[name]=people.get(name,0)+1
#
# bigcount=None
# bigname=None
# for name,count in people.items():
#     if bigcount is None or count>bigcount:
#         bigcount=count
#         bigname=name
#
#
# print bigname,bigcount


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
times=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From '):
        word = line.split()
        hour = word[5].split(':')[0]
        times[hour] = times.get(hour, 0) + 1

temp=sorted([(k,v) for k,v in times.items()])
for k,v in temp:
    print k,v