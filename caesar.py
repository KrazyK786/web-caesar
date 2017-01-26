

def encrypt(text,rot):
    """Your function should return the result of rotating each letter in the text by rot places to the right"""

    #list = text.split()
    newtext = ""
    for word in text:
        for letter in range(len(word)):
            if word[letter].isalpha() == True:
                newletter = rotate_character(word[letter],rot)
                newtext = newtext + newletter
            else:
                newtext = newtext + word[letter]
    return newtext


def alphabet_position(letter):
    import string
    """receives a letter (a string with only one alphabetic character)
    and returns the 0-based numerical position of that letter within the alphabet. It should be case-insensitive."""

    if ord(letter) < 97:
        pos = string.ascii_uppercase.index(letter)
    elif ord(letter) >= 97:
        pos = string.ascii_lowercase.index(letter)


    return pos

def rotate_character(char,rot):
    import string
    """receives a character char (a string of length 1), and an integer rot.
    Your function should return a new string of length 1, the result of rotating char by rot number of places to the right."""

    value = ord(char)

    #rotate = rot % 26

    if 65 <= value <= 90:
        newcharpos = alphabet_position(char)
        newcharpos += rot
        newcharpos = newcharpos % 26

        newchar = string.ascii_uppercase[newcharpos]

    elif 97 <= value <= 122:
        newcharpos = alphabet_position(char)
        newcharpos += rot
        newcharpos = newcharpos % 26

        newchar = string.ascii_lowercase[newcharpos]

    else:
        return char

    return newchar
