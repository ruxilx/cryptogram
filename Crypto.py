import string
import random
import wikiquote

def getquote():
    """
    This function accepts no parameters, and it will return the 
    author and quote of the day. It uses the wikiquote library.
    """
    quote, author = wikiquote.qotd()
    return quote, author

def createcipher():
    """
    This function accepts no parameters, and it creates a random cipher.
    It loops through the alphabet, and it uses random.choice to pick
    a random letter to be associated with the original letter.
    """
    alphdict = {}
    index = 0
    for letter in string.ascii_lowercase:
        ciph = random.choice(string.ascii_lowercase)
        if ciph not in alphdict.values():
            alphdict[letter] = ciph
        while letter not in alphdict.keys():
            ciph = random.choice(string.ascii_lowercase)
            if ciph not in alphdict.values():
                alphdict[letter] = ciph
    return alphdict

def encryptquote(quote):
    """
    This function accepts a string function, and it will return
    three parameters: the encrypted quote, original quote, and
    the cipher dictionary.
    """
    encryptedquote = ""
    qu = quote.lower()
    cipherdict = createcipher()
    for letter in qu:
        if letter in cipherdict.keys():
            encryptedquote += cipherdict[letter]
        else:
            encryptedquote += letter
    return encryptedquote, quote, cipherdict