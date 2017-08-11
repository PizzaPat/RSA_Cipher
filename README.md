# RSA Cipher
[![PyPI](https://img.shields.io/pypi/v/RSA-Cipher.svg)](https://pypi.python.org/pypi/RSA-Cipher)
[![PyPI](https://img.shields.io/pypi/dm/RSA-Cipher.svg)](https://pypi.python.org/pypi/RSA-Cipher)
[![Github All Releases](https://img.shields.io/github/downloads/PizzaPat/RSA_Cipher/total.svg)](https://github.com/PizzaPat/RSA_Cipher)

## Requirements:
[Python 3.6](https://www.python.org/downloads/release/python-361/)

[pip](https://bootstrap.pypa.io/get-pip.py)

## Installation:
```pip install rsa-cipher```

## Usage:
- Type ```rsa``` to start the program
- Encrypt
  - Message : Input the message you wish to encrypt with RSA method. The message can only be English alphabeths A-Z and white space. Numbers and other symbols may not be input
  - Enter prime number p / Enter prime number q : Input prime number that will be used for encryption. Make sure to input correct prime numbers. The numbers can be generated in option 3. Generate Prime Numbers
  - Pick positive integer range for encryption : Pick lower and upper bound for your private key 'e'. This will be the key to generate decryption key, by matching the candidate key 'e' key to 'd' key.
  - Result :
    - Encrypted Private Key will be the encryption key the user input. Decrypted Private Key will be the key the recipient have to input to decrypt the message. Public Key is obtainable for the public, it is insignificant to keep it secret.
- Decrypt
  - Enter Encrypted Message : Input the string of encrypted message. This should be a long string of number that the sender has sent to you.
  - Enter Decryption Key : Input the decryption key that is provided by sender. You may aquire this key in person to optimize your private communication
  - Enter Public Key : Input the public key that is given by the sender
- Generate Prime Numbers
  - Enter lower bound / Enter upper bound : Input the range between lower and upper bound to generate prime numbers to be used for prime p and prime q
- Check Prime Number
  - Enter Number : Input a number to check whether it is a prime number. The answer will be either True or False
- Notes
  - This will prompt the user for important information and any notes that the user should know about the program
- End Program
  - This will exit the program and go back to the command line
