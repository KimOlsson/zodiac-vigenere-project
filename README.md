# zodiac-vigenere-project

We use z408 solution on z340 and attempt to decrypt it using vigenere cipher with user submitted password

# Introduction

Serial killer known as Zodiac left behind some mysterious letters in 1969. His first ciphertext letter (sent in three pieces to different newspapers )
is better known as z408 letter (408 being the character amount). Solution to z408 was found really fast. However, few months later he sent another letter,
known as z340, which is now 50 years later, still unsolved. It is unknown if this z340 really contains any information, or is it just a 'prank'.
There has been some "solutions" to z340, but they havent really gotten much of a support on their validity.

# Motive behind this project

Just a fast over the weekend project for fun. My hunch says the solution to z340 requires a passphrase, but Im not sure if Vigenere cipher is the right tool,
nor what the exact passphrase might be.


# Usage
**PASSPHRASE** must be only letters from A-Z, due to how vigenere ciphers work.  
**ROTATION** parameters are numbers and expected to be between -26 and 26, and START < END  
```python main.py PASSPHRASE ROTATION_START ROTATION_END```  
This creates a file results_TIMESTAMP.txt
