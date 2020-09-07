{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "import random\n",
    "import wikiquote"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "def getquote():\n",
    "    \"\"\"\n",
    "    This function accepts no parameters, and it will return the \n",
    "    author and quote of the day. It uses the wikiquote library.\n",
    "    \"\"\"\n",
    "    quote, author = wikiquote.qotd()\n",
    "    return quote, author\n",
    "\n",
    "def createcipher():\n",
    "    \"\"\"\n",
    "    This function accepts no parameters, and it creates a random cipher.\n",
    "    It loops through the alphabet, and it uses random.choice to pick\n",
    "    a random letter to be associated with the original letter.\n",
    "    \"\"\"\n",
    "    alphdict = {}\n",
    "    index = 0\n",
    "    for letter in string.ascii_lowercase:\n",
    "        ciph = random.choice(string.ascii_lowercase)\n",
    "        if ciph not in alphdict.values():\n",
    "            alphdict[letter] = ciph\n",
    "        while letter not in alphdict.keys():\n",
    "            ciph = random.choice(string.ascii_lowercase)\n",
    "            if ciph not in alphdict.values():\n",
    "                alphdict[letter] = ciph\n",
    "    return alphdict\n",
    "\n",
    "def encryptquote(quote):\n",
    "    \"\"\"\n",
    "    This function accepts a string function, and it will return\n",
    "    three parameters: the encrypted quote, original quote, and\n",
    "    the cipher dictionary.\n",
    "    \"\"\"\n",
    "    encryptedquote = \"\"\n",
    "    qu = quote.lower()\n",
    "    cipherdict = createcipher()\n",
    "    for letter in qu:\n",
    "        if letter in cipherdict.keys():\n",
    "            encryptedquote += cipherdict[letter]\n",
    "        else:\n",
    "            encryptedquote += letter\n",
    "    return encryptedquote, quote, cipherdict"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
