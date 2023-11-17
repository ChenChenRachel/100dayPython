#forward direc
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def Decrypt(textinput,shiftinput):
    newword=""
    for text in textinput:
        position=alphabet.index(text)
        new_position = position+shiftinput
        new_letter=alphabet[new_position]
        newword+=new_letter
    print(newword)


Decrypt(text,shift)

#backword direc
def Decrypt(textinput,shiftinput):
    newword=""
    for text in textinput:
        position=alphabet.index(text)
        new_position = position-shiftinput
        new_letter=alphabet[new_position]
        newword+=new_letter
    print(newword)


Decrypt(text,shift)
