'''
Author: Aadil Hussain
Built on: Python 3.10.11
'''
# Assignment 2: Caesar Cypher Brute Force Hack

# Last year, you put together a program that would encrypt a message using
# the Caesar Cypher princple. In a Caesar Cypher, once you know the key
# (number of translated spots) then the message when appear unencrypted.

# Because the mafia doesn't want to get the 'key' through brute force and
# intimidation, they have hired you to create a program that will 'BRUTE
# FORCE' its way through the casear cypher by trying all possible outcomes.

# Given the encrypted message, design a program that will print every
# possible output - one of these outputs should contain the message

# The characters you may see as possible symbols include:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Here is the message to be decrypted:
MESSAGE = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
# Good luck to me

confirmed_shift = 0
message_indexed = []
for char in MESSAGE:
    message_indexed.append(SYMBOLS.find(char))

# main interation loop
for possible_shift in range(1, len(SYMBOLS)+1):
    # shift message by possible_shift value
    modded_message_indexes = []
    for item_index in range(len(message_indexed)):
        modded_message_indexes.append(message_indexed[item_index] + possible_shift)
        # bring out of range indexes within range
        if modded_message_indexes[item_index] > len(SYMBOLS)-1:
            excess = modded_message_indexes[item_index] - len(SYMBOLS)-1
            modded_message_indexes[item_index] = excess-1

    # make possible message
    decrypted_message = ''
    for modded_char_index in modded_message_indexes:
        decrypted_message += SYMBOLS[modded_char_index]

    # print possible message
    print(f"Shift{confirmed_shift}: {decrypted_message}")
    confirmed_shift += 1
