import random

from flask import Flask
app = Flask(__name__)


FLAG = 'https://vford.me/final-answers'
KEY  = 'It has been real'  # 16-ASCII-character key


def xor_strings_and_return_text(s1: str, s2: str) -> str:
    result = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(s1, s2)])
    return result


@app.route('/d/<ciphertext>')
def decrypt(ciphertext: str) -> str:
    bytes_object = bytes.fromhex(ciphertext)
    utf_8_string = bytes_object.decode('utf-8')

    message = ''
    for i in range(0, len(utf_8_string), 16):
        message += xor_strings_and_return_text(utf_8_string[i:i+16], KEY)

    return message


'''
XOR two strings character by character and return the result in hex
'''
def xor_strings_and_return_hex(s1: str, s2: str) -> str:
    result = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(s1, s2)])
    return result.encode('utf-8').hex()


@app.route('/<plaintext>')
def encrypt(plaintext: str) -> str:
    message = plaintext + FLAG
    
    while len(message) % len(KEY) != 0:
        # add random padding
        message += chr(random.randint(32, 128))

    encrypted = ''
    for i in range(0, len(message), 16):
        encrypted += xor_strings_and_return_hex(message[i:i+16], KEY)

    return encrypted


@app.route('/')
def home():
    return 'Please send your plaintext in the URL path. For example, <b>http://xorro.vford.com/this is a plaintext I want to encrypt</b>. In return, you will receive an encrypted message in <b>hex</b>. Your goal is to obtain the flag, given that the code that runs this whole server is the following:'
