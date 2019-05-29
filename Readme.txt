
###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################
       
	TOUTES LES 10MINS ON REPREND CES 5 ETAPES GRACE A LA COMMANDE crontab -e DANS LE SHELL BASH QUI EXECUTERA SES FICHIERS PYTHON

###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################



1- On execute camera.py qui prend une photo de la circulation et enregistre image.jpg

2- On execute count.py qui compte le nombre de voitures de la camera en traitant image.jpg et renvoie le nombre dans route1.txt 

route1.txt : contient le nombre de voitures de la route 1

route2.txt : contient le nombre de voitures de la route 2 ( qui est un fichier recu de la deuxieme carte root placee sur l'autre voie)

3- On envoie le fichier route1.txt vers l'autre carte root de la deuxieme voie
 
4- On execute compute.py qui fait la difference entre les entiers contenus dans route1.txt et route2.txt en renvoie le resultat dans final.txt
	final.txt =  0 : si route1 < route2
	final.txt =  1 : si route1 > route2

5- On execute raspi.py qui lit la valeur contenue dans final.txt et fait varie la duree d'allumage des feux vert et rouge en fonction de la valeur lue ( 0 ou 1)



###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################
