def palindrom():
    word='potop'
    print(word[::-1])

    if word == (word[::-1]):
        print ('Palindrom')
    else:
        print('Nie palindrom')

palindrom()