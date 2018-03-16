import string

def code_message(message,key):

    alphabet=' '+string.ascii_lowercase

    positions={}
    i=0

    for char in alphabet:
       positions[char]=i
       i+=1

    encoded_message=''

    for char in message.lower():
        pos = positions[char]
        encode = (pos + key)%27
        encoded_message+=alphabet[encode]

    return encoded_message
