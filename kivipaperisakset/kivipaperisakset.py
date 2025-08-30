#Kivi paperi sakset pähkinä discordista
#Author: Hembs
#Version 1.0

#importit
import random #tietokone pelaajaa varten.
import time #count downia varten

#settings
aseet = ["Kivi", "Paperi", "Sakset"]
minimipelaajat = 1
maksimipelaajat = 2
voittotaulukko = [ #tää o vähä hazard mut siis käytetään "aseet" arrayn indexejä 0 = Kivi, 1 = paperi jne...
    [0,2,1], #kivi voittaa sakset ja häviää paperille
    [1,0,2], #paperi voittaa kiven, häviää saksille
    [2,1,0] #sakset voittaa paperin, häviää kiville
]
#end of settings


def setupGame():
    #montako pelaajaa loop
    pelaajat = 0
    while not pelaajat:
        #haetaan user inputtia ja tarkastetaan että se on numero, muute hajoo ohjelma :D
        try:
            pelaajat = int(input(f"Montako pelaajaa? {minimipelaajat}, {maksimipelaajat}: ")) #pyydetään pelaaja määrä ja convertataan se suoraa integeriks.
        except ValueError:
            print("Syötetty arvo ei ole numero")
        if pelaajat <= maksimipelaajat and pelaajat: #tsekataa et o validi inputti
            break #jos oli validi ni si ulos loopista ja vetoja
        else:
            print (f"syötetyn arvon tulee olla välillä {minimipelaajat}, {maksimipelaajat}")
            pelaajat = 0 #looppi jatkuu jos inputti ei ollu validi
    startGame(pelaajat)
#end of setupGame


#tästä ihan tosissaan sit peli käyntii :D
def startGame(pelaajat):
    #tehää loopilla ase arraysta string
    aseet_string = "Valitse aseesi: "
    for idx, x in enumerate(aseet):
        aseet_string += str(idx) + " " + str(x) + ", "

    #montako pelaajaa, peli sen mukaan
    if pelaajat >= 2:
        pelaaja1 = int(input("Pelaaja 1 " + aseet_string))
        pelaaja2 = int(input("Pelaaja 2 " + aseet_string))
        friendGame(pelaaja1, pelaaja2)
    else:
        pelaaja1 = int(input("Pelaaja 1 " + aseet_string))
        botGame(pelaaja1)
#end of startGame


def botGame(pelaaja1):
    #voittajan voi hakee täs heti alus ni se tiietää jo ennen loppua :D
    winner = getWinner(pelaaja1, random.randrange(0, len(aseet))) #botti on toi random
    #count down niinku oikeessakin pelissä kivi... paperi... sakset...
    for x in aseet:
        print(x + "...")
        time.sleep(0.5)
    print(winner + " Voitti!")

#end of botGame
def friendGame(pelaaja1, pelaaja2):
    winner = getWinner(pelaaja1,pelaaja2)
    for x in aseet:
        print(x + "...")
        time.sleep(0.5)
    print(winner + " Voitti!")
#end of friendGame

def getWinner(pelaaja1, pelaaja2):
    if not pelaaja1 == pelaaja2:
        #tässä vähä mustaa magiaa
        if not voittotaulukko[pelaaja1][1] == pelaaja2:
            return "Pelaaja 2"
        else:
            return "Pelaaja 1"
    else:
        return "tasapeli"
#end of getWinner

#käynnistetään ohjelma lopussa, niin kerkee ladata kaikki functiot ja toimmii kivemmi.
setupGame()