```py
import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  😄   |
       |
       |
     ===''', '''
  +---+
  😥   |
  👕   |
       |
     ===''', '''
  +---+
  😰   |
 /👕   |
       |
     ===''', '''
  +---+
  😩   |
 /👕\  |
    |
     ===''', '''
  +---+
  😩   |
 /👕\  |
  🩳   |   
 /    |
 

     ===''', '''
  +---+
  😫   |
 /👕\  |
  🩳   |
 / \  |
     ===''', '''
  +---+
 [😱   |
 /👕\  |
  🩳   |
 / \   |
     ===''', '''
  +---+
 [💀]  |
 /👕\  |
  🩳   |
 /  \  |
     ===''']
words = {'Colores':'rojo naranja amarillo verde azul indigo violeta blanco negro marron'.split(),
'Formas':'cuadrado triangulo rectangulo circulo elipse rombo trapecio cheuron pentagono hexagono heptagono octagono'.split(),
'Frutas':'manzana naranja limon lima pera sandía uva toronja cereza platano melon mango fresa tomate'.split(),
'Animales':'murcielago oso castor gato puma cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela león lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja zorrillo calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()}

def getRandomWord(wordDict):
    ''' Esta función devuelve una cadena aleatoria del diccionario pasado de listas de cadenas, y también la clave.'''
    
    # First, randomly select a key from the dictionary:ewewe
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('letras perdidas:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letterse
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Adivina una letra.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor ingrese una sola letra.')
        elif guess in alreadyGuessed:
            print('Ya has adivinado esa letra. elegir de nuevo.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor ingrese una LETRA.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('y')
hangman = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      

"""
print(hangman)

difficulty = 'X'
while difficulty not in 'EMH':
  print('Enter Dificultad: E - Facil, M - Normal, H - Dificil')
  difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('La palabra secreta está en el conjunto: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('¡Sí! La palabra secreta es"' + secretWord + '"! ¡Usted ha ganado!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
```