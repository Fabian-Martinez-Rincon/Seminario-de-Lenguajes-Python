import os
import random


'''
   ┌╔────────┐
   │║        Ô
   │║       └┼┘
   │║        │
   │║       ┌┴┐
   │║   ┌─────────┐
   │║   │         │
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
'''

FRAMES = {
    'base' : (
        '   ┌╔─────────┐',
        '   │║',
        '   │║',
        '   │║',
        '   │║',
        '   │║    ┌─────────┐',
        '   │║    │         │',
        '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀'
    ),
    'levels' : (
        { 1 : '   │║         Ô ' },
        { 2 : '   │║        └┼ ' },
        { 2 : '   │║        └┼┘' },
        { 3 : '   │║        ┌┴ ' },
        { 3 : '   │║        ┌┴┐' }
    ),
    'loose' : '''
   ┌╔─────────┐
   │║         │
   │║         │          
   │║         Ø      YOU
   │║        ┌┼┐          ║  ╔╗ ╔═ ╔═
   │║    ┌─┐ ┌┴┐ ┌─┐      ║  ║║ ╚╗ ╠═
   │║    │         │      ╚═ ╚╝ ═╝ ╚═
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''',
    'win' : '''
   ┌╔─────────
   │║         
   │║         O
   │║        ┌┼┐      YOU
   │║        ┌┴┐          ║   ║ ¤ ╔═╗
   │║    ┌───┴─┴───┐      ║ ║ ║ ║ ║ ║
   │║    │         │      ╚═╩═╝ ╚ ╚ ╚
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
'''
}

WORDS_DICT = {
    'Colors' :'red orange yellow green blue indigo violet white black brown'.split(),
    'Shapes' :'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),
    'Fruits' :'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(),
    'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()
}



def clear_console():
    os.system('cls')

def getRandomWord():
    
    # First, randomly select a key from the dictionary:
    key = random.choice(list(WORDS_DICT.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(WORDS_DICT[key]) - 1)

    return [key, WORDS_DICT[key][wordIndex]]

def displayBoard(missed_letters, correct_letters, secret_word, frame):

    level = len(missed_letters)
    if level > 0:
        update =  FRAMES['levels'][level-1]
        for key in update.keys():
            frame[key] = update[key]
    
    for line in frame:
        print(line)

    print('Letras erroneas:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)): # replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(already_guessed):
    while True:
        guess = input('Letra: ').lower()
        if len(guess) != 1:
            print('Se pidio una letra, intenta nuevamente')
        elif guess in already_guessed:
            print('Ya dijiste esa letra, intenta nuevamente')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Se pidio una letra, intenta nuevamente')
        else:
            return guess

def get_difficulty():
    clear_console()
    difficulty = ' '
    while difficulty not in 'FMD':
        print('Ingrese dificultad:\n    F - Facil\n    M - Medio\n    D - Dificil\n')
        difficulty = input('Opcion:  ').upper()
    return difficulty

def play_again():
    answer = input('\nQueres jugar de nuevo?\n  Si | No\nOpcion: ')
    return answer.lower().startswith('s')

def show_menu():
    print(
        'EL AHORCADO\n\n'\
        'Ahora si vamos a jugar\n'\
        'Elija una opcion:\n'\
        '  J - Jugar\n'\
        '  S - Salir\n'\
        )
    answer = input('Opcion: ').lower()
    while answer not in 'jugarsalir':
        print(f'{answer} no es una respuesta valida, intente denuevo')
        answer = input('Opcion: ').lower()

    return answer in 'jugar'

def reset(difficulty):
    missed_letters = ''
    correct_letters = ''
    
    secret_set, secret_word  = getRandomWord()

    match difficulty:
        case 'F':
            correct_letters = secret_word[random.randrange(len(secret_word))]
            correct_letters += secret_word[random.randrange(len(secret_word))]
        case 'M':
            correct_letters = secret_word[random.randrange(len(secret_word))]
    
    frame = list(FRAMES['base'])

    return [missed_letters, correct_letters, secret_set, secret_word, frame]

def develop_game(missed_letters, correct_letters, secret_set, secret_word, frame):
    game_done = False
    while not game_done:
        clear_console()
        print('El tipo de la palabra es: ' + secret_set)
        displayBoard(missed_letters, correct_letters, secret_word, frame)

        # Let the player type in a letter.
        guess = getGuess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess

            # Check if the player has won
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                clear_console()
                print(FRAMES['win'])
                print('\nSi!\nLa palabra secreta era: "' + secret_word + '"!\nGanaste')
                game_done = True
        else:
            missed_letters = missed_letters + guess

            # Check if player has guessed too many times and lost.
            if len(missed_letters) == 6:
                clear_console()
                print(FRAMES['loose'])
                print('Te quedaste sin intentos!\nDespues de ' + str(len(missed_letters)) + ' fallos y ' + str(len(correct_letters)) + ' correctas adivinanzas,\nla palabra era "' + secret_word + '"')
                game_done = True

def app():
    play = show_menu()

    while play:
        difficulty = get_difficulty()
        missed_letters, correct_letters, secret_set, secret_word, frame = reset(difficulty)

        develop_game(missed_letters, correct_letters, secret_set, secret_word, frame)

        play = play_again()



app()

clear_console()
print('EL AHORCADO\n\nGracias por jugar <3')