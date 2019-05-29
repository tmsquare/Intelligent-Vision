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