import ciphers as c
import time
import sys

# Passphrase must be at least as long as the cipher
def multiply_passphrase(c, p):
  long_passphrase = ""
  for i in range(len(c)):
    if len(c) > len(long_passphrase):
      long_passphrase += p
  return long_passphrase

# For each passphrase letter find it's index on the alphabeth. 
# Then from the row of tabula recta corresponding to the index
# find the ciphertext letter, then take that index and 
# find the corresponding letter on the alphabeth.
def vigenere_decrypt(cipher, tabula_recta, passphrase):
  long_passphrase = multiply_passphrase(cipher, passphrase)
  alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  plaintext_result = ""

  for i in range(len(cipher)):
    passphrase_char = long_passphrase[i]
    if passphrase_char == '?':
        plaintext_result += '?'
        continue

    for row in range(len(tabula_recta)):
      
      if passphrase_char == alphabeth[row]:
        row_index = tabula_recta[row].find(cipher[i])
        
        plaintext_result += alphabeth[row_index] if row_index != -1 else '?'
        break
  return plaintext_result

def writeToResults(results):
  timestamp = int(time.time())
  filename = "results_{0}.txt".format(timestamp)
  
  with open('./{0}'.format(filename), 'w') as file:
    file.write(results)
  print("Wrote results to a file {0}".format(filename))

def tryDifferentTabulas(cipher, passphrase, rotate_start = -3, rotate_end = 3, rotate_first_row = False):
  all_results = ""
  new_pass = passphrase
  for i in range(rotate_start, rotate_end):
    tabula_recta = c.tabula('A', 'Z', i, rotate_first_row)
    solution_attempt = vigenere_decrypt(cipher, tabula_recta, new_pass)
    pretty = c.prettyString(solution_attempt)
    info = "rotation {}, tabula first row rotated: {}, pass: {}\n".format(i, ("yes" if rotate_first_row else "no"), new_pass)
    all_results += (17*"#") + "\n" + info + (17 * "-") + "\n" + pretty + "\n"
  return all_results


def main():
  # Get the cipher data
  z408p = c.z408plain()
  z408c = c.z408cipher()
  z340c = c.z340cipher()

  # Dictionary for z408 cipher->plaintext solution
  z408_dict = c.cipherToPlainDict(z408c, z408p)

  # Use the z408 solution on z340
  z340translation_temp = c.translateCipherToPlain(z340c, z408p, z408_dict)
  z340_with_z408_solution = ''.join(z340translation_temp)

  passphrase = str(sys.argv[1]).upper()
  isPassphraseAllowed = passphrase.isalpha()

  if isPassphraseAllowed:
    results = tryDifferentTabulas(z340_with_z408_solution, passphrase, -2, 2)
    writeToResults(results)
  else:
    print("Passphrase must contain letters from A-Z!")

if __name__ == "__main__":
  main()