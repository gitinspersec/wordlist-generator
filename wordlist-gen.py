import json
import itertools

config = json.load(open('config.json'))

def generate_wordlist(min_length, max_length):
    wordlist = []
    digits = '0123456789'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special = '!@#$%^&*()_+'
    charsets = ''
    if config['digits']:
        charsets += digits
    if config['lowercase']:
        charsets += lowercase
    if config['uppercase']:
        charsets += uppercase
    if config['special']:
        charsets += special
    for length in range(min_length, max_length + 1):
        for word in itertools.product(charsets, repeat=length):
            print(''.join(word))
            wordlist.append(''.join(word))

    return wordlist

if __name__ == '__main__':
    min_length = int(input('Enter minimum length: '))
    max_length = int(input('Enter maximum length: '))
    wordlist = generate_wordlist(min_length, max_length)
    with open('wordlist.txt', 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    print('Wordlist generated successfully!')