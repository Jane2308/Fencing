import random

def get_word():
    words = ['Dianne',
             'Tomas',
             'Fencing',
             'Sabre',
             'Netherlands',
             'Zwolle',
             'Carlow',
             'Python',
             'Cookies',
             'Alpaca',
             'Queen bee',
             'Plants',
             'Walks',
             'Letters',
             'Ireland',
             'Stars',
             'Tart',
             'Snowman',
             'Snowball',
             'Monster']
    return random.choice(words).upper()

# Zit de letter in het woord
def check(word, guesses, guess):
    guess = guess.upper()
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += ' _ '
        if letter == guess:
            matches += 1
    if matches > 1:
        print('Yes! The word contains', matches,'"' + guess + '"' + 's')
    elif matches == 1:
        print ('Yes! The word contains the letter "' + guess + '"')
    else:
        print('Sorry! The word does not contains the letter "' + guess + '"')

    return status

# Frame voor galgje
def main():
    word = get_word()
    guesses = []
    guessed = False
    print ('The word contains', len(word), 'letters.')
    while not guessed:
        text = 'Please enter a letter or a {}-letter word.'.format(len(word))
        guess = input(text)
        guess = guess.upper()
        if guess in guesses:
            print ('You already guessed "' + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print ('Sorry, wrong answer!')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word, guesses, guess)
            if result == word:
                guessed = true
            else:
                print(result)
        else:
            print ('Invalid entry.')

    print('Yes, you did it! The word is' , word +'! You did it in', len(guesses),'tries')

main()
