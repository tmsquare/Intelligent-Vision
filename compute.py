number1 = 0
number2 = 1

with open("route1.txt", "r") as g:
  a=g.read()

with open("route2.txt", "r") as f:
  b=f.read()

c = int(a)-int(b)


if (c<0):
    with open('final.txt', 'w') as h:
          h.write('%d' % number1)
else:
    with open('final.txt', 'w') as h:
          h.write('%d' % number2)

b = int(a)+int(b)
with open('history.txt', 'a') as h:
          h.write('%d' % b)
          h.write("\n")
          
def tail(file, n=1, bs=1024):
    f = open(file)
    f.seek(0,2)
    l = 1-f.read(1).count('\n')
    B = f.tell()
    while n >= l and B > 0:
            block = min(bs, B)
            B -= block
            f.seek(B, 0)
            l += f.read(block).count('\n')
    f.seek(B, 0)
    l = min(l,n)
    lines = f.readlines()[-l:]
    f.close()
    return lines

lastEvaluation = 0
lines = tail("history.txt", 3)

for line in lines:
    lastEvaluation += int(line)
    
with open('chatbotdata.txt', 'w') as h:
          h.write('%d' % lastEvaluation)
 

          