import json
import itertools

# Carrega a configuração
config = json.load(open('config.json'))

def generate_wordlist(min_length, max_length):
    wordlist = []
    digits = '0123456789'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special = '!@#$%^&*()_+'
    charsets = ''
    
    # Se houver uma palavra personalizada, usamos apenas seus caracteres
    custom_word = config.get('custom_word')
    if custom_word:
        # Opcional: remove duplicatas, mantendo a ordem
        charsets = ''.join(dict.fromkeys(custom_word))
    else:
        if config.get('digits'):
            charsets += digits
        if config.get('lowercase'):
            charsets += lowercase
        if config.get('uppercase'):
            charsets += uppercase
        if config.get('special'):
            charsets += special

    # Gera as combinações para cada tamanho entre min_length e max_length
    for length in range(min_length, max_length + 1):
        for word in itertools.product(charsets, repeat=length):
            generated_word = ''.join(word)
            print(generated_word)
            wordlist.append(generated_word)

    return wordlist

if __name__ == '__main__':
    min_length = int(input('Enter minimum length: '))
    max_length = int(input('Enter maximum length: '))
    wordlist = generate_wordlist(min_length, max_length)
    with open('wordlist.txt', 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    print('Wordlist generated successfully!')
