from gpiozero import LED
from time import sleep

with open("final.txt", "r") as f:
  var=f.read()
  
var = int(var)

a=6
b=3
c=1

red = LED(22)
amber = LED(27)
green = LED(17)


boolean= True

x = 6

'''
Chaque tour de feu prend y= a+b+c.

Ainsi on calibre la valeur de x avec la frequence du crontab.

Exemple:
Si le crontab se fait toute les minutes=60s et que y = 10s
Dans ce cas la boucle for doit s'executer 6 fois d'ou x=6.

Ainsi apres chaque minute, on fait un allumage uniquement en
fonction de la valeur contenue dans final.txt puis le programme
s'interrompt et on excecute un nouveau script (new crontab) sans perdre le fil.. en
changeant juste les durees d'allumage contenues dans a et b 



for i in range(0,x): 
    if(var == 0):
        red.on()
        sleep(a)
        red.off()
        amber.on()
        sleep(c)
        amber.off()
        green.on()
        sleep(b)
        green.off()
        amber.on()
        sleep(c)
        amber.off()
    else:
        red.on()
        sleep(b)
        red.off()
        amber.on()
        sleep(c)
        amber.off()
        green.on()
        sleep(a)
        green.off()
        amber.on()
        sleep(c)
        amber.off()'''
while True:
    
    red.on()
    sleep(1)
    red.off()
    amber.on()
    sleep(1)
    amber.off()
    green.on()
    sleep(1)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
