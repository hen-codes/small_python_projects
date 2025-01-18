"""""
Vier Gewinnt
7 mal 6 (Spielfeld)
"""""
from gturtle import *

makeTurtle()
hideTurtle()

#Variablen
holesize = 25
xstandard = 0-6*holesize
ystandard = -1*holesize 
spieler1 = "orange"
spieler2 = "firebrick"

#Listen und Dictionaries
spalte1 = [0, 0, 0, 0, 0, 0]
spalte2 = [0, 0, 0, 0, 0, 0]
spalte3 = [0, 0, 0, 0, 0, 0]
spalte4 = [0, 0, 0, 0, 0, 0]
spalte5 = [0, 0, 0, 0, 0, 0]
spalte6 = [0, 0, 0, 0, 0, 0]
spalte7 = [0, 0, 0, 0, 0, 0]

werte = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def werte_anzeigen():
    print(".................)")
    print(spalte1)
    print(spalte2)
    print(spalte3)
    print(spalte4)
    print(spalte5)
    print(spalte6)
    print(spalte7)
    print(werte)

def spielfeld(holesize):
    setPos(xstandard, 3.5*holesize)
    for i in range(6):
        setX(xstandard)
        for i in range(7):
            setPenColor("gainsboro")
            penDown()
            dot(holesize)
            penUp()
            setHeading(90)
            forward(holesize*2)
            delay(10)
        setHeading(-180)
        forward(holesize*1.5)

def ch_spalte(farbe, holesize, weristdran):
    wo = int(input("Spalte (1-7)"))
    if wo < 1 or wo > 7:
        ch_spalte(farbe, holesize, weristdran)
        
    #setY(ystandard)
    #setX(xstandard+wo*holesize*2-2*holesize)
    #setPenColor(farbe)
    #penDown()
    #dot(holesize)
    #penUp()
    delay(500)
    zuweisen(wo, weristdran)
    #abwechseln(weristdran)
    

def abwechseln(ak_spieler_num):
    ak_spieler_num += 1
    ak_spieler_num = ak_spieler_num%2
    if ak_spieler_num == 0:
        ch_spalte(spieler1, holesize, ak_spieler_num)
    else:
        ch_spalte(spieler2, holesize, ak_spieler_num)

def zuweisen(spalte, ak_spieler_num):
    ersetzt = False
    wherex = 0
    wherey = 0 
    if spalte == 1:
        for i in range(6):
            if ersetzt == False:
                if spalte1[i] == 0:
                    spalte1[i] = ak_spieler_num + 1
                    werte[i] = ak_spieler_num +1
                    ersetzt = True
                    wherey = i-1
    elif spalte == 2:
        for i in range(6):
            if ersetzt == False:
                if spalte2[i] == 0:
                    spalte2[i] = ak_spieler_num + 1
                    werte[i + 6] = ak_spieler_num + 1
                    ersetzt = True
                    wherey = i-1
    elif spalte == 3:
        for i in range(6):
            if ersetzt == False:
                if spalte3[i] == 0:
                    spalte3[i] = ak_spieler_num + 1
                    werte[i + 12] = ak_spieler_num + 1
                    ersetzt = True
                    wherey = i-1
    elif spalte == 4:
        for i in range(6):
            if ersetzt == False:
                if spalte4[i] == 0:
                    spalte4[i] = ak_spieler_num + 1
                    werte[i +18] = ak_spieler_num + 1
                    ersetzt = True
                    wherey = i-1
    elif spalte == 5:
        for i in range(6):
            if ersetzt == False:
                if spalte5[i] == 0:
                    spalte5[i] = ak_spieler_num + 1
                    werte[i + 24] = ak_spieler_num + 1
                    ersetzt = True
                    wherey = i-1
    elif spalte == 6:
        for i in range(6):
            if ersetzt == False:
                if spalte6[i] == 0:
                    spalte6[i] = ak_spieler_num + 1
                    werte[i + 30] = ak_spieler_num + 1
                    ersetzt = True
                    wherey = i-1

    elif spalte == 7:
        for i in range(6):
            if ersetzt == False:
                if spalte7[i] == 0:
                    spalte7[i] = ak_spieler_num + 1
                    werte[i + 36] = ak_spieler_num + 1
                    ersetzt = True
                    wherey = i-1
    if ersetzt == False:
        #print("Die Spalte ist bereits voll. Wähle eine neue Spalte!") #NEU
        #delay(800) #NEU (Um vor der Eingabe die obenstehende Nachricht lesen zu können)
        #ch_spalte()
        #ch_spalte(farbe, holesize, weristdran)
        #frage nach einer neuen Spalte
        pass
    if ersetzt == True:
        wherex = spalte
        berechne_position(wherex, wherey, ak_spieler_num)    
        
        
def berechne_position(wherex, wherey, ak_spieler_num):
    setX(xstandard+(wherex-1)*holesize*2)
    setY(ystandard+(wherey-1)*1.5*holesize)
    if ak_spieler_num == 0: 
        setPenColor(spieler1)
    else:
        setPenColor(spieler2)
    penDown()
    dot(holesize)
    penUp()
    delay(1000) 
    # werte_anzeigen()
    check_winner(ak_spieler_num)
    abwechseln(ak_spieler_num)

# auf Sieg prüfen

def check_winner(ak_spieler_num): 
    for x in range(0, 24):
        if werte[x] != 0:
            if werte[x] == werte[x + 6] == werte[x + 12] == werte[x + 18]:
                for i in range(10): 
                    print("Spieler", ak_spieler_num + 1, "hat gewonnen!")
                    delay(10)
                delay(99999999999)
    for x in range(0, 36, 6) and (1, 37, 6) and (2, 38, 6):
        if werte[x] != 0:
             if werte[x] == werte[x+ 1] == werte[x + 2] == werte[x + 3]:
                for i in range(10): 
                    print("Spieler", ak_spieler_num + 1, "hat gewonnen!")
                    delay(10)
                delay(99999999999)
    for x in range(0, 18, 6) and (1, 19, 6) and (2, 20, 6):
        if werte[x] != 0:
             if werte[x] == werte[x+ 7] == werte[x + 14] == werte[x + 21]:
                for i in range(10): 
                    print("Spieler", ak_spieler_num + 1, "hat gewonnen!")
                    delay(10)
                delay(99999999999)
    for x in range(3, 21, 6) and (4, 22, 6) and (5, 23, 6):
        if werte[x] != 0:
             if werte[x] == werte[x+ 5] == werte[x + 10] == werte[x + 15]:
                for i in range(10): 
                    print("Spieler", ak_spieler_num + 1, "hat gewonnen!")
                    delay(10)
                delay(99999999999)
    


# Programm ausführen

spielfeld(holesize)
delay(1000)
abwechseln(1)







