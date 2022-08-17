from gtts import gTTS
import os
import random
import time
import np
import keyboard
import readchar

language = "es-us"
running = True
currentGame = False
velocidad = 4

def printMatrix (bingo, matrix):
    print('')
    for x in bingo:
        print(x, end='\t')
    print('\n', end='')

    for x in matrix:
        for y in x:
            print(y, end='\t')
        print('\n', end='')

def canto(texto):
    speech = gTTS(text=texto, lang=language, slow = False)
    speech.save("canto.mp3")
    os.system("start canto.mp3")

def resetCurrentGame():
    global currentGame
    currentGame = False

def exitGame():
    global running
    running = False
    print("Cerrando aplicacion")

keyboard.on_press_key("space", lambda _:resetCurrentGame())
keyboard.on_press_key("x", lambda _:exitGame())

mensajeInicial = False

while (running == True):
    canto("Selecciona la velocidad")
    print("Selecciona la velocidad del juego")
    print("1. Lento")
    print("2. Rapido")
    print("3. Muy Rapido")
    velocidadInput = input()

    if velocidadInput == '1': velocidad = 4
    if velocidadInput == '2': velocidad = 3
    if velocidadInput == '3': velocidad = 1

    message = "Comenzando el juego"
    print(message)
    canto(message)
    time.sleep(3)

    currentGame = True
    bingo = ["B", "I", "N", "G", "O"]
    arrB = [*range(1, 16)]
    arrI = [*range(16, 31)]
    arrN = [*range(31, 46)]
    arrG = [*range(46, 61)]
    arrO = [*range(61, 76)]

    calledB = []
    calledI = []
    calledN = []
    calledG = []
    calledO = []

    while(currentGame == True):

        if mensajeInicial == False:
            message = "Presiona la tecla 'espacio' cuando alguien diga 'bingo' o la tecla 'x' para terminar de jugar"
            print(message)
            mensajeInicial = True

        number = 0
        for x in bingo:
            if x == "B":
                number = random.choice(arrB)
                arrB.remove(number)
                calledB.append(number)
            if x == "I":
                number = random.choice(arrI)
                arrI.remove(number)
                calledI.append(number)
                if currentGame == False: break
            if x == "N":
                number = random.choice(arrN)
                arrN.remove(number)
                calledN.append(number)
                if currentGame == False: break
            if x == "G":
                number = random.choice(arrG)
                arrG.remove(number)
                calledG.append(number)
                if currentGame == False: break
            if x == "O":
                number = random.choice(arrO)
                arrO.remove(number)
                calledO.append(number)
                if currentGame == False: break
            
            text = f'{x}{number}'
            canto(text)
            time.sleep(velocidad)
        
        if len(arrB) == 0 and len(arrI) == 0 and len(arrN) == 0 and len(arrG) == 0 and len(arrO) == 0:
            currentGame = False

        if currentGame == False:
            calledB.sort()
            calledI.sort()
            calledN.sort()
            calledG.sort()
            calledO.sort()

            for i in range(0, 5):
                if i > len(calledB)-1:
                    calledB.append('')

                if i > len(calledI)-1:
                    calledI.append('')

                if i > len(calledN)-1:
                    calledN.append('')

                if i > len(calledG)-1:
                    calledG.append('')

                if i > len(calledO)-1:
                    calledO.append('')

            validarArray = np.column_stack((calledB, calledI, calledN, calledG, calledO))
            printMatrix(bingo, validarArray)
            message = "Presiona cualquier tecla para continuar"
            print(message)
            readchar.readchar()
            readchar.readchar()
            message = "Empezando un nuevo juego"
            print(message)
            canto(message)