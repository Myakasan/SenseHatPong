#Initialisation du SenseHat
from sense_hat import SenseHat
sense = SenseHat()
#Nettoyage de l'ecran
sense.clear(0,0,0)
#Initialisation du pixel de départ
x=4
y=4
sense.set_pixel(x,y,255,255,255)
#Si le SenseHat est bien initialisé alors je récupère les informations
#du joystick et les print en console.
while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
