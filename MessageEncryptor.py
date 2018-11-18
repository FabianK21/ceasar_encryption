# MessageEncryption.py
# This is a Programm that should encrypt in an choosable format
# To decrypt the message you need to use the same key as it was encrypted

# Initialise
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
newMessage = ''
newCharacter = ''

##################################
# Menu
##################################
print('Menu:')
print('1: Encrypt message')
print('2: Decrypt message')
myOption = int(input('Choose your option: '))


##################################
# Encrypt
##################################
if myOption == 1:
    myMessage = input('Please enter your message: ')                        # Get message
    myKey = int(input('Please enter the Key you want to encrypt with: '))   # Get encryption key

    for character in myMessage:
        if character in alphabet:                                           # Check if in alphabet
            position = alphabet.find(character)                             # Locate position
            newPosition = (position + myKey) % 52                           # Get new postition an check overflow
            newCharacter = alphabet[newPosition]                            # Get new character
            newMessage += newCharacter                                      # Allign all characters in to one message

        elif character == ' ':                                              # Mind spaces
            newCharacter = ' '
            newMessage +=newCharacter

        else:
            newMessage += character                                         # Add non alphabetic characters without changes

    print('Your new message is: ' + newMessage)                             # Print new message


##################################
# Decrypt
##################################
elif myOption == 2:
    myMessage = input('Please enter your message: ')                        # Get message
    myKey = int(input('Please enter the Key you want to decrypt with: '))   # Get decryption key

    for character in myMessage:
        if character in alphabet:
            position = alphabet.find(character)                             # Locate position
            newPosition = (position - myKey) % 52                           # Get new postition an check overflow
            newCharacter = alphabet[newPosition]                            # Get new character
            newMessage += newCharacter                                      # Allign all characters in to one message

        elif character == ' ':                                              # Mind spaces
            newCharacter = ' '
            newMessage += newCharacter

        else:
            newMessage += character                                         # Add non alphabetic characters without changes

    print('Your new message is: ' + newMessage)                             # Print new message


##################################
# Error
##################################
else:
    print('Error: Option unknown')
