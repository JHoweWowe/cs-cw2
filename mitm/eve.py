import sys
import os

from common import *
from const import *

# Import argparser
import argparse

# Add optional arguments for flags
parser = argparse.ArgumentParser()
parser.add_argument("--relay", help="Relay message from Bob to Alice and Alice back to Bob", action="store_true")
parser.add_argument("--break-heart", help="Become the ultimate love destroyer and break both hearts", action="store_true")
parser.add_argument("--custom", help="The ball is yours. Manipulate both users' messages", action="store_true")
args = parser.parse_args()

dialog = Dialog('print')

# WHOLE IDEA: Bob sends message first, then Alice (NOT VICE VERSA)

# Setup communication channel as Bob
bobPlayer = 'bob'
bobSocket, bobAES = setup(bobPlayer, BUFFER_DIR, BUFFER_FILE_NAME)
dialog.think('Eve thinks: "Yeee nice, getting there..."')

# Rename buffer file
src = BUFFER_DIR + BUFFER_FILE_NAME
dst = BUFFER_DIR + 'new_buffer'
os.rename(src, dst)

# Setup communication channel as Alice
alicePlayer = 'alice'
aliceSocket, aliceAES = setup(alicePlayer, BUFFER_DIR, BUFFER_FILE_NAME)
dialog.think('Eve thinks: "Hehe, it works!"')

bob_msg = receive_and_decrypt(aliceAES, aliceSocket) # Msg from Bob

if (args.relay):
    encrypt_and_send(bob_msg, bobAES, bobSocket) # Bob sends msg
    dialog.chat('Bob said: "{}"'.format(bob_msg))
    dialog.info('Message sent! Waiting for reply...')

    alice_msg = receive_and_decrypt(bobAES, bobSocket) # Eve obtains msg from Alice
    dialog.chat('Alice said: "{}"'.format(alice_msg))
    encrypt_and_send(alice_msg, aliceAES, aliceSocket)

elif (args.break_heart):
    bob_msg = BAD_MSG['bob'] # BAD_MSG is a dictionary and 'bob' is a key

    encrypt_and_send(bob_msg, bobAES, bobSocket) # Bob sends 'I hate you!' instead of original msg
    dialog.chat('Bob said: "{}"'.format(bob_msg))
    dialog.info('Message sent! Waiting for reply...')

    alice_msg = receive_and_decrypt(bobAES, bobSocket) # Eve obtains msg from Alice
    dialog.chat('Alice said: "{}"'.format(alice_msg))
    encrypt_and_send(BAD_MSG['alice'], aliceAES, aliceSocket) # Alice sends 'You broke my heart...'
    
elif (args.custom):
    dialog.chat('Bob slurred: "{}"'.format(bob_msg)) # Original msg
    #dialog.info('Message sent! Waiting for reply...')

    dialog.prompt('Input what you would like Bob to say to Alice') # Input customized msg instead
    input_bob_to_alice_msg = input()

    encrypt_and_send(input_bob_to_alice_msg, bobAES, bobSocket) # Sends customized msg to Alice as "Bob"

    alice_msg = receive_and_decrypt(bobAES, bobSocket)
    dialog.chat('Alice slurred: "{}"'.format(alice_msg))

    dialog.prompt('Input what you would like Alice to say to Bob')
    input_alice_to_bob_msg = input()
    encrypt_and_send(input_alice_to_bob_msg, aliceAES, aliceSocket)

else:
    print("Please choose a valid flag")
    sys.exit(1)

tear_down(bobSocket, BUFFER_DIR, 'new_buffer')
tear_down(aliceSocket, BUFFER_DIR, BUFFER_FILE_NAME)

## Steps:
## 1. Add flags from ArgumentParser [DONE]
## 2. Configure OS buffer file for two separate communication channels [DONE]
## 3. Use encrypt and decrypt library methods from alice.py and bob.py for flags [DONE]