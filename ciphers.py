from collections import deque
# Ciphers from: http://zodiackillerciphers.com/wiki/index.php?title=Webtoy%27s_transcription_scheme

def z408plain():
  return  "ILIKEKILLINGPEOPLEBECAUSEITISSOMUCHFUNITISMOREFUNTHANKILLINGWILDGAMEINTHEFORRESTBECAUSEMANISTHEMOSTDANGERTUEANAMALOFALLTOKILLSOMETHINGGIVESMETHEMOSTTHRILLINGEXPERENCEITISEVENBETTERTHANGETTINGYOURROCKSOFFWITHAGIRLTHEBESTPARTOFITISTHAEWHENIDIEIWILLBEREBORNINPARADICESNDALLTHEIHAVEKILLEDWILLBECOMEMYSLAVESIWILLNOTGIVEYOUMYNAMEBECAUSEYOUWILLTRYTOSLOIDOWNORSTOPMYCOLLECTINGOFSLAVESFORMYAFTERLIFEEBEORIETEMETHHPITI"

def z408cipher():
  # Backslashes were used, so we had to escape them, \ -> \\
  return  "9%P/Z/UB%kOR=pX=BWV+eGYF69HP@K!qYeMJY^UIk7qTtNQYD5)S(/9#BPORAU%fRlqEk^LMZJdr\\pFHVWe8Y@+qGD9KI)6qX85zS(RNtIYElO8qGBTQS#BLd/P#B@XqEHMU^RRkcZKqpI)Wq!85LMr9#BPDR+j=6\\N(eEUHkFZcpOVWI5+tL)l^R6HI9DR_TYr\\de/@XJQAP5M8RUt%L)NVEKH=GrI!Jk598LMlNA)Z(PzUpkA9#BVW\\+VTtOP^=SrlfUe67DzG%%IMNk)ScE/9%%ZfAP#BVpeXqWq_F#8c+@9A9B%OT5RUc+_dYq_^SqWVZeGYKE_TYA9%#Lt_H!FBX9zXADd\\7L!=q_ed##6e5PORXQF%GcZ@JTtq_8JI+rBPQW6VEXr9WI6qEHM)=UIk"

def z340cipher():
  return  "HER>pl^VPk|1LTG2dNp+B(#O%DWY.<*Kf)By:cM+UZGW()L#zHJSpp7^l8*V3pO++RK2_9M+ztjd|5FP+&4k/p8R^FlO-*dCkF>2D(#5+Kq%;2UcXGV.zL|(G2Jfj#O+_NYz+@L9d<M+b+ZR2FBcyA64K-zlUV+^J+Op7<FBy-U+R/5tE|DYBpbTMKO2<clRJ|*5T4M.+&BFz69Sy#+N|5FBc(;8RlGFN^f524b.cV4t++yBX1*:49CE>VUZ5-+|c.3zBK(Op^.fMqG2RcT+L16C<+FlWB|)L++)WCzWcPOSHT/()p|FkdW<7tB_YOB*-Cc>MDHNpkSzZO8A|K;+"

def printCipher(text, width=17):
  for i in range(len(text)):
    if (i % width == 0 and i != 0):
      print()
    print(text[i], end='')
  print()

def prettyString(text, width=17):
  pretty = ""
  for i in range(len(text)):
    if (i % width == 0 and i != 0):
      pretty += "\n"
    pretty += text[i]
  return pretty + "\n"

def cipherToPlainDict(c, p):
  cipherToPlain = {}
  for i in range(len(c)):
    if c[i] not in cipherToPlain:
      cipherToPlain[c[i]] = p[i]  # If cipher letter is not in dict, add it as key:value (cipher:plain)

  return cipherToPlain

def translateCipherToPlain(c, p, c2p_dict):
  if len(c) > len(p):
    raise Exception('cipher cannot be longer than plaintext')
  translatedMessage = []
  for i in range(len(c)):
    current = c2p_dict.get(c[i], "?")
    translatedMessage.append(current)
  return translatedMessage

# deed02392 had skeleton for this in github, I made some adjustments.
def tabula(start = 'A', end = 'Z', rotation = -1, first_row_rotated = False):
  ascii_min = ord(start)
  ascii_max = ord(end)

  # make list with deque so we can use rotate() later
  # deque may not be optimal solution for such a small table
  d = deque(chr(x) for x in range(ascii_min, ascii_max + 1))
  loop_length = len(d) if first_row_rotated else len(d)-1
  result_list = [] if first_row_rotated else [''.join(d)]

  for i in range(loop_length):
      d.rotate(rotation)
      result_list.append(''.join(d))
  return result_list